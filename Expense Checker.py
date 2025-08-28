import json
from datetime import datetime, timedelta

# ==============================
# Expense Class
# ==============================
class Expense:
    def __init__(self, ammount=0, category="", date=None, description=""):
        self.ammount = ammount
        self.category = category
        self.date = date if date else datetime.today().date()
        self.description = description

    def __str__(self):
        return f"Expense(Amount: {self.ammount}, Category: {self.category}, Date: {self.date}, Description: {self.description})"

    def to_dict(self):
        return {
            "Amount": self.ammount,
            "Category": self.category,
            "Date": str(self.date),
            "Description": self.description
        }


# ==============================
# Recurring Expense Class
# ==============================
class Recurring_expense(Expense):
    def __init__(self):
        self.ammount = int(input("Enter the amount: "))
        self.category = input("Enter the category: ")
        self.date = datetime.strptime(input("Enter the date (YYYY-MM-DD): "), "%Y-%m-%d").date()
        self.description = input("Enter the description: ")
        self.frequency = input("Enter the frequency (daily, weekly, monthly, yearly): ").lower()

    def next_occurrence(self):
        if self.frequency == "daily":
            return self.date + timedelta(days=1)
        elif self.frequency == "weekly":
            return self.date + timedelta(weeks=1)
        elif self.frequency == "monthly":
            return self.date + timedelta(days=30)  # Approximation
        elif self.frequency == "yearly":
            return self.date + timedelta(days=365)
        else:
            raise ValueError("Invalid frequency. Use daily, weekly, monthly, or yearly.")

    def to_dict(self):
        d = super().to_dict()
        d["Frequency"] = self.frequency
        return d


# ==============================
# Expense Manager
# ==============================
class ExpenseManager:
    def __init__(self, filename="D:\\fileX\\Record.json", autosave=True):
        self.filename = filename
        self.autosave = autosave
        self.expenses = []
        self.load_from_file()

    def add_expense(self, expense):
        if not isinstance(expense, Expense):
            raise TypeError("Only Expense instances can be added.")
        self.expenses.append(expense)
        if self.autosave:
            self.save_expenses()

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        for exp in self.expenses:
            print(exp)

    def save_expenses(self):
        with open(self.filename, "w") as f:
            json.dump([expense.to_dict() for expense in self.expenses], f, indent=4)

    def load_from_file(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)

            # Ensure data is always a list of dicts
            if isinstance(data, dict):
                data = [data]
            elif not isinstance(data, list):
                print("⚠️ Invalid JSON format. Resetting file...")
                data = []

            self.expenses = []
            for item in data:
                if not isinstance(item, dict):
                    continue  # Skip invalid entries
                try:
                    date_obj = datetime.strptime(item["Date"], "%Y-%m-%d").date()
                except Exception:
                    date_obj = datetime.today().date()

                if "Frequency" in item:  # recurring
                    exp = Recurring_expense.__new__(Recurring_expense)
                    exp.ammount = item.get("Amount", 0)
                    exp.category = item.get("Category", "")
                    exp.date = date_obj
                    exp.description = item.get("Description", "")
                    exp.frequency = item.get("Frequency", "monthly")
                else:  # normal
                    exp = Expense.__new__(Expense)
                    exp.ammount = item.get("Amount", 0)
                    exp.category = item.get("Category", "")
                    exp.date = date_obj
                    exp.description = item.get("Description", "")
                self.expenses.append(exp)

        except FileNotFoundError:
            self.expenses = []
        except json.JSONDecodeError:
            print("⚠️ Corrupted JSON file. Resetting...")
            self.expenses = []

    def search_by_category(self, category):
        found = [exp for exp in self.expenses if exp.category.lower() == category.lower()]
        if not found:
            print("No expenses found in this category.")
        else:
            for exp in found:
                print(exp)


# ==============================
# Demo Menu
# ==============================
if __name__ == "__main__":
    manager = ExpenseManager()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Normal Expense")
        print("2. Add Recurring Expense")
        print("3. View All Expenses")
        print("4. Search by Category")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amt = int(input("Enter amount: "))
            cat = input("Enter category: ")
            date = datetime.strptime(input("Enter date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            desc = input("Enter description: ")
            exp = Expense(amt, cat, date, desc)
            manager.add_expense(exp)

        elif choice == "2":
            exp = Recurring_expense()
            manager.add_expense(exp)

        elif choice == "3":
            manager.view_expenses()

        elif choice == "4":
            cat = input("Enter category to search: ")
            manager.search_by_category(cat)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")
