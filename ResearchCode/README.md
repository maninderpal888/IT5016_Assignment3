
# Requisition Management System

## Overview
The Requisition Management System is a simple console application that allows users to register, display, and manage requisitions. This system helps track the status of requisitions submitted by staff, providing an overview of approved, pending, and not approved requests.

## Features
- Register new requisitions with details such as date, request ID, staff ID, staff name, total amount, status, and approval reference number.
- Display all registered requisitions along with their details and status.
- Show statistics including total requisitions, number of approved, pending, and not approved requisitions.

## Requirements
- Python 3.10

## How to Run
1. Clone the repository or download the source code.
2. Open a terminal and navigate to the directory containing the `Research.py` file.
3. Run the application using the following command:
   ```bash
   python Research.py
4.Follow the on-screen prompts to register requisitions and view statistics.

## Usage
Choose an option from the menu:
Register a new requisition: Input the details for a new requisition.
Display all requisitions: View all registered requisitions and their statuses.
Exit: Close the application.

## Example 
1. Register a new requisition
2. Display all requisitions
3. Exit
Enter your choice: 1
Enter date: 2024-09-25
Enter request ID: 101
Enter staff ID: S123
Enter staff name: John Doe
Enter total: 150.00
Enter status (approved/pending/not approved): pending
Enter approval reference number: REF12345

## Statistics
After exiting the application, the system will display the following statistics:

Total number of requisitions submitted.
Total number of approved requisitions.
Total number of pending requisitions.
Total number of not approved requisitions.


