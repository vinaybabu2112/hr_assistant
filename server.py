from mcp.server.fastmcp import FastMCP
from typing import List, Dict, Optional
from employee_manager import EmployeeManager, EmployeeCreate
from leave_manager import LeaveManager, LeaveApplyRequest
from meeting_manager import MeetingManager
from ticket_manager import TicketManager, TicketCreate
from utils import seed_services
from emails import EmailSender
import os
from dotenv import load_dotenv

mcp = FastMCP('atliq-hr-asistant')

employee_manager = EmployeeManager()
leave_manager  = LeaveManager()
ticket_manager = TicketManager()
meeting_manager = MeetingManager()

seed_services(employee_manager, leave_manager, meeting_manager, ticket_manager)
emailer = EmailSender(
    smtp_server="smtp.gmail.com",
    port=587,
    username=os.getenv("CB_EMAIL"),
    password=os.getenv("CB_EMAIL_PWD"),
    use_tls=True
)

@mcp.tool()
def add_employee(emp_name:str, manager_id:str, email:str) -> str:
    """
    Add a new employee to the HRMS system.
    :param emp_name: Employee name
    :param manager_id: Manager ID (optional)
    :return: Confirmation message
    """
    emp = EmployeeCreate(
        emp_id=employee_manager.get_next_emp_id(),
        name=emp_name,
        manager_id=manager_id,
        email=email
    )
    employee_manager.add_employee(emp)
    return f"Employee {emp_name} added successfully."

@mcp.tool()
def get_employee_details(name: str) -> Dict[str, str]:
    """
    Get employee details by name.
    :param name: Name of the employee
    :return: Employee ID and manager ID
    """
    matches = employee_manager.search_employee_by_name(name)

    if len(matches) == 0:
        raise ValueError(f"No employees found with name {name}.")

    emp_id = matches[0]
    emp_details = employee_manager.get_employee_details(emp_id)
    return emp_details

@mcp.tool()
def send_email(subject: str, body: str, to_emails: List[str] | str, from_email: Optional[str] = None) -> None:
    """
    Send an email using the configured email sender.
    :param subject: Email subject
    :param body: Email body
    :param to_emails: List of recipient email addresses or a single email address
    :param from_email: Optional sender email address
    """
    emailer.send_email(
        subject=subject,
        body=body,
        to_emails=to_emails,
        from_email=from_email
    )
    return "Email sent successfully."

@mcp.tool()
def create_ticket(emp_id: str,item: str, reason: str) -> str:
    ticket_req = TicketCreate(
        emp_id=emp_id,
        item=item,
        reason=reason
    )   
@mcp.tool()
def get_leave_history(emp_id: str) -> List[Dict[str, str]]:
    """
    Get leave history for an employee.
    :param emp_id: Employee ID
    :return: List of leave records
    """
    return leave_manager.get_leave_history(emp_id)

@mcp.tool()
def apply_leave(emp_id: str, leave_dates: List[str]) -> str:
    """
    Apply for leave for an employee.
    :param emp_id: Employee ID
    :param leave_dates: List of leave dates in ISO format
    :return: Confirmation message
    """
    req = LeaveApplyRequest(emp_id=emp_id, leave_dates=leave_dates)
    return leave_manager.apply_leave(req)
@mcp.tool()
def get_leave_balance(emp_id: str) -> str:
    """
    Get the leave balance for an employee.
    :param emp_id: Employee ID
    :return: Leave balance message
    """
    return leave_manager.get_leave_balance(emp_id)



@mcp.tool()
def meeting_schedule(emp_id: str, meeting_dt: str, topic: str) -> str:
    """
    Schedule a meeting for an employee.
    :param emp_id: Employee ID
    :param meeting_dt: Scheduled date and time of the meeting in ISO format
    :param topic: Topic of the meeting
    :return: Confirmation message
    """
    return meeting_manager.schedule_meeting(emp_id, meeting_dt, topic)



@mcp.prompt("onboard_new_employee")
def onboard_new_employee(employee_name: str,Email_id: str, manager_name: str) -> str:
    return f"""Onboard a new employee with the following details:
    - Name: {employee_name}
    -Email: {Email_id}
    - Manager Name: {manager_name}
    Steps to follow:
    - Add the employee to the HRMS system. 
    - Send a onboarding email to the employee with manager name.
    - Send a welcome email to the employee.
    - Raise Ticket for new Laptop, id card and other necessary items.
    """


@mcp.prompt("leave_management")
def leave_management(employee_id: str, leave_dates: List[str]) -> str:
    return f"""Manage leave for employee with ID {employee_id}:
    - Check leave balance.
    - Apply for leave on the following dates: {', '.join(leave_dates)}.
    - Get leave history for the employee.
    """

if __name__ == "__main__":
    mcp.run(transport="stdio")
    
