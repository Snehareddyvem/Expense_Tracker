
import csv
import os
from datetime import date


EXPENSES_FILE = "expenses.csv"


class Expense:

    def __init__(self, expense_id, expense_date, category, description, amount):
        self.expense_id = expense_id
        self.expense_date = expense_date
        self.category = category
        self.description = description
        self.amount = amount


class ExpenseTracker:

    def __init__(self):
        self.create_file()

    # ----------------------------------------
    # CREATE CSV FILE
    # ----------------------------------------

    def create_file(self):

        if not os.path.exists(EXPENSES_FILE):

            with open(EXPENSES_FILE, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "expense_id",
                    "date",
                    "category",
                    "description",
                    "amount"
                ])

    # ----------------------------------------
    # GET NEXT EXPENSE ID
    # ----------------------------------------

    def get_next_id(self):

        highest_id = 0

        with open(
            EXPENSES_FILE,
            "r",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                try:

                    expense_id = int(row["expense_id"])

                    if expense_id > highest_id:
                        highest_id = expense_id

                except ValueError:

                    continue

        return highest_id + 1

    # ----------------------------------------
    # ADD EXPENSE
    # ----------------------------------------

    def add_expense(self):

        # Automatically generate ID
        expense_id = self.get_next_id()

        print(f"Expense ID: {expense_id}")

        # Automatically use today's date
        expense_date = str(date.today())

        print(f"Date: {expense_date}")

        category = input("Enter Category: ")

        description = input("Enter Description: ")

        try:

            amount = float(
                input("Enter Amount: ")
            )

        except ValueError:

            print("Invalid amount.")
            return

        if amount < 0:

            print("Amount cannot be negative.")
            return

        with open(
            EXPENSES_FILE,
            "a",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                expense_id,
                expense_date,
                category,
                description,
                amount
            ])

        print("Expense added successfully!")

    # ----------------------------------------
    # DISPLAY ALL EXPENSES
    # ----------------------------------------

    def display_expenses(self):

        with open(
            EXPENSES_FILE,
            "r",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            expenses = list(reader)

        if not expenses:

            print("No expenses recorded.")
            return

        print("\n========== ALL EXPENSES ==========")

        for expense in expenses:

            print(f"\nExpense ID: {expense['expense_id']}")
            print(f"Date: {expense['date']}")
            print(f"Category: {expense['category']}")
            print(f"Description: {expense['description']}")
            print(f"Amount: ₹{float(expense['amount']):.2f}")

            print("-" * 35)

    # ----------------------------------------
    # VIEW EXPENSES FOR A DATE
    # ----------------------------------------

    def view_by_date(self):

        expense_date = input(
            "Enter date (YYYY-MM-DD): "
        )

        found = False

        total = 0

        print(
            f"\n===== EXPENSES FOR {expense_date} ====="
        )

        with open(
            EXPENSES_FILE,
            "r",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            for expense in reader:

                if expense["date"] == expense_date:

                    found = True

                    amount = float(expense["amount"])

                    total += amount

                    print(
                        f"{expense['expense_id']} - "
                        f"{expense['category']} - "
                        f"{expense['description']} - "
                        f"₹{amount:.2f}"
                    )

        if not found:

            print("No expenses found for this date.")

        else:

            print("-" * 40)
            print(f"Total: ₹{total:.2f}")

    # ----------------------------------------
    # VIEW EXPENSES BY CATEGORY
    # ----------------------------------------

    def view_by_category(self):

        category = input(
            "Enter category: "
        ).lower()

        found = False

        total = 0

        print(
            f"\n===== CATEGORY: {category.upper()} ====="
        )

        with open(
            EXPENSES_FILE,
            "r",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            for expense in reader:

                if expense["category"].lower() == category:

                    found = True

                    amount = float(expense["amount"])

                    total += amount

                    print(
                        f"{expense['date']} - "
                        f"{expense['description']} - "
                        f"₹{amount:.2f}"
                    )

        if not found:

            print("No expenses found in this category.")

        else:

            print("-" * 40)
            print(f"Total spent on {category}: ₹{total:.2f}")

    # ----------------------------------------
    # TOTAL EXPENSE
    # ----------------------------------------

    def total_expense(self):

        total = 0

        with open(
            EXPENSES_FILE,
            "r",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            for expense in reader:

                total += float(expense["amount"])

        print("\n========== TOTAL EXPENSE ==========")
        print(f"Total spent: ₹{total:.2f}")

    # ----------------------------------------
    # MONTHLY REPORT
    # ----------------------------------------

    def monthly_report(self):

        month = input(
            "Enter month (YYYY-MM): "
        )

        total = 0

        count = 0

        print(
            f"\n===== EXPENSE REPORT: {month} ====="
        )

        with open(
            EXPENSES_FILE,
            "r",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            for expense in reader:

                if expense["date"][:7] == month:

                    count += 1

                    amount = float(expense["amount"])

                    total += amount

                    print(
                        f"{expense['date']} - "
                        f"{expense['category']} - "
                        f"{expense['description']} - "
                        f"₹{amount:.2f}"
                    )

        if count == 0:

            print("No expenses found for this month.")

        else:

            print("-" * 40)
            print(f"Number of expenses: {count}")
            print(f"Total spent: ₹{total:.2f}")

    # ----------------------------------------
    # DELETE EXPENSE
    # ----------------------------------------

    def delete_expense(self):

        expense_id = input(
            "Enter Expense ID to delete: "
        )

        found = False

        expenses = []

        with open(
            EXPENSES_FILE,
            "r",
            newline=""
        ) as file:

            reader = csv.DictReader(file)

            for expense in reader:

                if expense["expense_id"] == expense_id:

                    found = True

                else:

                    expenses.append(expense)

        if not found:

            print("Expense not found.")
            return

        # Rewrite CSV file
        with open(
            EXPENSES_FILE,
            "w",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "expense_id",
                "date",
                "category",
                "description",
                "amount"
            ])

            for expense in expenses:

                writer.writerow([
                    expense["expense_id"],
                    expense["date"],
                    expense["category"],
                    expense["description"],
                    expense["amount"]
                ])

        print("Expense deleted successfully!")


# ============================================
# MAIN PROGRAM
# ============================================

expense_tracker = ExpenseTracker()


while True:

    print("\n")
    print("===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. Display All Expenses")
    print("3. View Expenses by Date")
    print("4. View Expenses by Category")
    print("5. View Total Expense")
    print("6. View Monthly Report")
    print("7. Delete Expense")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        expense_tracker.add_expense()

    elif choice == "2":

        expense_tracker.display_expenses()

    elif choice == "3":

        expense_tracker.view_by_date()

    elif choice == "4":

        expense_tracker.view_by_category()

    elif choice == "5":

        expense_tracker.total_expense()

    elif choice == "6":

        expense_tracker.monthly_report()

    elif choice == "7":

        expense_tracker.delete_expense()

    elif choice == "8":

        print("Thank you!")
        break

    else:

        print("Invalid choice.")