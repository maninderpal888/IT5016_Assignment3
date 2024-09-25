
# Requisition Management System

## Overview
The Requisition Management System is a simple console application that allows users to register, display, and manage requisitions. This system helps track the status of requisitions submitted by staff, providing an overview of approved, pending, and not approved requests.

## Features
- **Register Requisitions**: Users can input various details of a requisition, including date, request ID, staff ID, staff name, total amount, status, and approval reference number.
- **Display Requisitions**: The application allows users to view all registered requisitions, complete with their details and current statuses.
- **Status Check**: Each requisition can be checked for its current status—approved, pending, or not approved.
- **Statistics Summary**: At any time, users can view a summary of requisition statistics, including the total number of requisitions submitted and the breakdown of their statuses.

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

1.Total number of requisitions submitted.
2.Total number of approved requisitions.
3.Total number of pending requisitions.
4.Total number of not approved requisitions.



# Software Design Principles in Relation to the Requisition Research Code

## Overview of Software Design Principles
Software design principles are guidelines that help developers create software that is maintainable, scalable, and robust. In the context of the "Requisition" project, several key design principles have been applied to enhance the quality and functionality of the application.

## 1. Single Responsibility Principle (SRP)
The **Single Responsibility Principle** states that a class should have only one reason to change, meaning it should focus on a single responsibility. In the "Requisition" code, the `Requisition` class is dedicated solely to managing requisition data and operations. 

### Application to Code:
- **Class Focus**: The `Requisition` class encapsulates all attributes related to a requisition, such as date, request ID, staff ID, and status. By doing so, it maintains a clear and focused purpose.
- **Maintainability**: If changes are required in requisition management (like adding a new attribute), we only need to modify this single class, making maintenance straightforward.

## 2. Open/Closed Principle (OCP)
The **Open/Closed Principle** asserts that software entities (like classes, modules, and functions) should be open for extension but closed for modification. This principle allows new functionality to be added without altering existing code.

### Application to Code:
- **Future Enhancements**: The design of the `Requisition` class allows for future enhancements, such as adding new methods to handle different requisition types or statuses. Developers can create subclasses that extend the `Requisition` functionality without changing the existing codebase.
- **Flexibility**: For example, if we later want to implement a system for categorizing requisitions (e.g., by department), we can achieve this through subclassing or additional methods.

## 3. Liskov Substitution Principle (LSP)
The **Liskov Substitution Principle** states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program. This principle emphasizes that subclasses should behave in a way that does not alter the expected functionality.

### Application to Code:
- **Subclassing Potential**: While the current code uses a single class, it is designed with future subclassing in mind. For instance, if we create a subclass for special requisitions (like emergency requests), this subclass should seamlessly integrate into the existing system.
- **Behavior Consistency**: As long as the new subclass adheres to the existing interface (methods and properties), it can be used interchangeably with the base `Requisition` class.

## 4. Interface Segregation Principle (ISP)
The **Interface Segregation Principle** suggests that no client should be forced to depend on methods it does not use. In other words, interfaces should be small and specific to the needs of clients.

### Application to Code:
- **Minimal Interface**: The `Requisition` class exposes only the necessary methods required for requisition management, such as `display_requisition()` and `check_status()`. This prevents unnecessary complexity and keeps the class focused.
- **Ease of Use**: Users of the class only interact with relevant methods, making it simpler to understand and utilize.

## 5. Dependency Inversion Principle (DIP)
The **Dependency Inversion Principle** states that high-level modules should not depend on low-level modules; both should depend on abstractions. This principle promotes decoupling, making systems easier to maintain and extend.

### Application to Code:
- **Future Abstractions**: Although the current code does not implement interfaces or abstract classes, the design allows for such extensions in future iterations. For example, if we want to add a database layer for storing requisition data, we can define an interface for data access that both the `Requisition` class and the data layer depend on.
- **Decoupling**: By adhering to this principle, the application can evolve without being tightly coupled to specific implementations, enhancing its adaptability.

## Conclusion
The "Requisition" research project effectively employs key software design principles, which contribute to its maintainability, scalability, and overall functionality. By adhering to these principles, the project not only fulfills its current requirements but also lays the groundwork for future enhancements and adaptations in requisition management. Understanding and applying these principles is crucial for developing robust software solutions in any domain, including research and organizational processes.


