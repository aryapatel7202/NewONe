# Personal Expense Tracker
# Author: Arya Patel S.
# A simple CLI project to keep track of daily expenses
# Built for learning and solving a real-world problem

import csv
from datetime import datetime
import matplotlib.pyplot as plt

CSV_FILE = "expenses.csv"

# Create CSV file if it doesn't exist
def init_csv():
    try:
        with open(CSV_FILE, 'x', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])
    except FileExistsError:
        pass  # File already exists


# Add a new expense entry
def add_expense():
    print("\n--- Add New Expense ---")
    date = datetime.now().strftime('%Y-%m-%d')
    category = input("Category (e.g., Food, Bills, Transport): ")
    try:
        amount = float(input("Amount (₹): "))
    except ValueError:
        print("Invalid amount. Please enter a valid number.\n")
        return
    desc = input("Short description (optional): ")

    with open(CSV_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, desc])

    print("Expense saved successfully.\n")


# Show all recorded expenses
def view_expenses():
    print("\n--- All Expenses ---\n")
    try:
        with open(CSV_FILE, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(", ".join(row))
    except FileNotFoundError:
        print("No expense file found.\n")


# Show category-wise pie chart
def show_chart():
    print("\n--- Spending Breakdown Chart ---")
    totals = {}

    try:
        with open(CSV_FILE, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cat = row['Category']
                try:
                    amt = float(row['Amount'])
                    totals[cat] = totals.get(cat, 0) + amt
                except:
                    continue  # Skip any row with invalid amount

        if totals:
            labels = list(totals.keys())
            amounts = list(totals.values())

            plt.figure(figsize=(7, 5))
            plt.pie(amounts, labels=labels, autopct='%1.1f%%', startangle=140)
            plt.title("Expense Breakdown by Category")
            plt.axis('equal')
            plt.show()
        else:
            print("No expenses found to generate chart.\n")

    except FileNotFoundError:
        print("Expense file not found.\n")


# CLI menu loop
def main():
    init_csv()
    while True:
        print("====== Personal Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Chart")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            show_chart()
        elif choice == '4':
            print("Goodbye! Stay consistent with your tracking.")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
