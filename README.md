# Expense_Tracker
## Project Overview

The Expense Tracker is a simple and user-friendly Python application designed to manage daily expenses efficiently. It allows users to add, view, and delete expense records while storing the data in a CSV file.

The application also provides total, daily, monthly, and category-wise expense tracking. It reduces manual calculations and helps users organize their expense information efficiently.

## Features

* Add new expense records
* Automatically generate Expense ID
* Automatically record the current date
* View all expenses
* View expenses by date
* View expenses by category
* Calculate total expenses
* Generate monthly expense reports
* Delete expenses using Expense ID
* Store expense data in a CSV file
* Validate expense amount input

## Tech Stack

* **Programming Language:** Python
* **Concepts:** Object-Oriented Programming (OOP)
* **File Handling:** CSV
* **Python Modules:** `csv`, `os`, `datetime`
* **Storage:** CSV file (`expenses.csv`)

## Project Structure

```text
Expense-Tracker/
│
├── expense_tracker.py
├── expenses.csv
└── README.md
```

## Setup and Run

### 1. Install Python

Make sure Python is installed on your system.

Check the Python version:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone https://github.com/Snehareddyvem/Expense_Tracker
```

### 3. Open the Project Folder

```bash
cd Expense-Tracker
```

### 4. Run the Application

```bash
python Expense_Tracker.py
```

The application will display a menu where users can choose different expense management options.

## Environment Variables

This project does not require any environment variables.

```text
Environment variables: Not applicable
```

## API / Database Notes

This project does not use any external API or database.

Expense records are stored locally in:

```text
expenses.csv
```

The CSV file contains:

* Expense ID
* Date
* Category
* Description
* Amount

## Team Member Contributions

### Vem Sneha

* Designed and developed the Expense Tracker application.
* Implemented the Python classes and functions.
* Implemented CSV file storage and data handling.
* Added expense calculation and reporting features.
* Tested the application with different inputs.
* Prepared project documentation and presentation.

## Conclusion

The Expense Tracker demonstrates the practical use of Python programming, Object-Oriented Programming, CSV file handling, and basic data management. The project provides a simple solution for recording and analyzing personal expenses while reducing manual calculations.
