# Atliq HR Assistant

A comprehensive HR Assistant system designed to streamline common HR operations, reducing the workload on HR personnel.

## Table of Contents

  * [About the Project](https://www.google.com/search?q=%23about-the-project)
  * [Features](https://www.google.com/search?q=%23features)
  * [Getting Started](https://www.google.com/search?q=%23getting-started)
      * [Prerequisites](https://www.google.com/search?q=%23prerequisites)
      * [Installation](https://www.google.com/search?q=%23installation)
      * [Configuration](https://www.google.com/search?q=%23configuration)
  * [Usage](https://www.google.com/search?q=%23usage)
  * [Project Structure](https://www.google.com/search?q=%23project-structure)
  * [Contributing](https://www.google.com/search?q=%23contributing)
  * [License](https://www.google.com/search?q=%23license)
  * [Contact](https://www.google.com/search?q=%23contact)

## About the Project

The Atliq HR Assistant is an intelligent system built to automate and simplify various human resources tasks. Its primary goal is to **decrease the workload on HR personnel** by providing self-service functionalities for employees and efficient management tools for HR. This system leverages an AI assistant framework (FastMCP) to interact with different HR modules, making operations more intuitive and efficient.

## Features

The system offers a range of functionalities to manage employees, leaves, and internal requests, along with communication capabilities:

  * **Employee Management**:
      * Add new employees to the HRMS system.
      * [cite\_start]Retrieve detailed employee information by name or ID[cite: 1].
      * [cite\_start]Search for employees by name with fuzzy matching[cite: 1].
      * [cite\_start]Identify an employee's manager[cite: 1].
      * [cite\_start]List an employee's direct reports[cite: 1].
  * **Leave Management**:
      * Check an employee's current leave balance.
      * Apply for leave on specified dates.
      * View an employee's leave history.
  * **Meeting Management**:
      * Schedule meetings for employees.
      * Retrieve an employee's scheduled meetings.
      * Cancel existing meetings.
  * **Ticket Management**:
      * Create new internal tickets for various requests (e.g., IT equipment, ID Cards, Laptops etc).
      * Update the status of existing tickets (e.g., Open, In Progress, Closed, Rejected).
      * List tickets, with options to filter by employee or status.
  * **Email Communication**:
      * Send emails programmatically for notifications and updates (e.g., onboarding emails).
  * **Automated Workflows**:
      * **New Employee Onboarding**: A defined prompt to handle the complete onboarding process, including adding the employee to the system, sending welcome emails, and raising tickets for necessary items.
      * **Leave Request Management**: A prompt to manage leave requests, encompassing balance checks, application, and history retrieval.

## Getting Started

To get a copy of the project up and running on your local machine for development and testing purposes, follow these steps.

### Prerequisites

  * Python 3.9+
  * `pip` (Python package installer)
  * Claude Desktop for MCP integration

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/atliq-hr-assistant.git
    cd atliq-hr-assistant
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

The system uses environment variables for sensitive information, such as email credentials.

1.  **Create a `.env` file** in the root directory of the project.
2.  **Add the following environment variables:**
    ```
    CB_EMAIL="your_email@gmail.com"
    CB_EMAIL_PWD="your_app_password" # Use an app-specific password for Gmail or similar
    ```
      * **Note on `CB_EMAIL_PWD`**: If you are using Gmail, you will need to generate an "App password" rather than using your regular Gmail password, especially if you have 2-Factor Authentication enabled. Refer to Google's documentation for "Sign in with app passwords" for more details.

## Usage

The `server.py` file contains the main application logic and exposes the functionalities as tools for the FastMCP agent.

1.  **Run the server:**

    ```bash
    python server.py
    ```

    [cite\_start]The `seed_services` function will automatically populate the in-memory managers with dummy data upon startup, allowing you to test functionalities immediately[cite: 1].

2.  **Interact with the system:**
    Since this project uses `FastMCP` with `stdio` transport, you will interact with the HR Assistant via your console's standard input/output. You can type commands or natural language queries that the agent will interpret and execute using the available tools.

    **Examples (when the `server.py` is running and you are prompted for input):**

      * `onboard new employee John Doe with email john.doe@atliq.com and manager Sarah Johnson`
      * `get employee details for Michael Chen`
      * `what is the leave balance for E004?`
      * `apply leave for E005 on 2025-08-01 and 2025-08-02`
      * `create a ticket for E003 for a new monitor because the old one is broken`
      * `schedule a meeting for E001 on 2025-08-05T10:00:00 about Project Alpha`
      * `send an email to john.doe@atliq.com with subject "Welcome to Atliq!" and body "Dear John, Welcome to the team!"`

## Project Structure

```
├── server.py             # Main FastMCP application, tool definitions, and prompt handlers
├── employee_manager.py   # Manages employee data (add, search, details, manager/reports)
├── leave_manager.py      # Handles leave balances, applications, and history
├── meeting_manager.py    # Manages meeting scheduling and cancellations
├── ticket_manager.py     # Manages IT/other internal tickets
├── schemas.py            # Pydantic models for data validation and structure
├── emails.py             # Email sending utility
├── utils.py              # Utility functions, including data seeding for managers
├── requirements.txt      # Python dependencies
└── .env                  # Environment variables (for email credentials)
```

## Contributing

Contributions are welcome\! Please feel free to open issues or submit pull requests.



## 🙌 Acknowledgments

* Inspired by [Codebasics GEN AI Projects](https://github.com/codebasics/)
* Data sourced from Kaggle and public loan datasets
* Credit to Dhaval Patel, Hemanand Vadivel & the Codebasics community for guidance

---

## 👤 Author

**Vinay Babu Muttireddy**
🔗 [GitHub](https://github.com/vinaybabu2112)

---

> ⭐ If you found this helpful, give it a star and share with fellow data scientists!
