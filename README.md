Expense Tracker Project
📌 Overview

The Expense Tracker is a simple Python project that helps users record, manage, and analyze their daily and recurring expenses. It allows you to add expenses, categorize them, save them to a file, reload them when the program restarts, and search expenses by category.

This project is designed for beginners in Python and demonstrates concepts like:

Object-Oriented Programming (OOP)

File handling with JSON

Date and time handling

Basic menus and user interaction in the terminal

⚙️ Features

Add Normal Expense

Enter amount, category, date, and description.

Example: Food, Transport, Rent, Shopping, etc.

Add Recurring Expense

Enter amount, category, date, description, and frequency (daily, weekly, monthly, yearly).

Automatically calculates the next occurrence date.

View All Expenses

Nicely displays all recorded expenses with details.

Example:

Expense(Amount: 100, Category: Food, Date: 2025-08-17, Description: Pizza)
Expense(Amount: 500, Category: Rent, Date: 2025-08-01, Description: Apartment)


Search by Category

Filter and view only expenses of a specific category.

Save & Load Automatically

All expenses are saved in a JSON file (Record.json).

When the program restarts, previous records are loaded back automatically.

🛠️ Technologies Used

Python 3

JSON for saving/loading data

Datetime module for handling dates and recurring expenses

📂 Project Structure

Expense class → Represents a single expense (amount, category, date, description).

Recurring_expense class → Extends Expense with frequency and next occurrence.

ExpenseManager class → Manages all expenses (add, view, search, save, load).

Menu (main loop) → Provides user interface to interact with the program.

🚀 How to Run

Save the script as ExpenseTracker.py.

Run it in terminal:

python ExpenseTracker.py


A menu will appear with options to add/view/search expenses.

Records are automatically saved in Record.json.

📖 Example Usage
--- Expense Tracker ---
1. Add Normal Expense
2. Add Recurring Expense
3. View All Expenses
4. Search by Category
5. Exit


✅ Add your food, rent, transport, or any other expense.
✅ Data is safely stored even after closing the program.# Python-Projects-No-2-OOP-Expense-Checker.
