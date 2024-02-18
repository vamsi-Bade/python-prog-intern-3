import csv
from collections import defaultdict
from datetime import datetime

expenses = defaultdict(list)

def add_expense(amount, description, category):
    date = datetime.now().strftime('%Y-%m-%d')
    expenses[date].append({'amount': amount, 'description': description, 'category': category})
    print("Expense added successfully.")

def save_expenses():
    with open('expenses.csv', 'w', newline='') as csvfile:
        fieldnames = ['date', 'amount', 'description', 'category']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for date, expense_list in expenses.items():
            for expense in expense_list:
                writer.writerow({'date': date, 'amount': expense['amount'], 'description': expense['description'], 'category': expense['category']})

def load_expenses():
    try:
        with open('expenses.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                expenses[row['date']].append({'amount': row['amount'], 'description': row['description'], 'category': row['category']})
    except FileNotFoundError:
        print("No expenses found.")

def view_monthly_summary(month, year):
    total_spent = 0
    for date, expense_list in expenses.items():
        if datetime.strptime(date, '%Y-%m-%d').month == month and datetime.strptime(date, '%Y-%m-%d').year == year:
            for expense in expense_list:
                total_spent += float(expense['amount'])
    print(f"Total expenses for {datetime(year, month, 1).strftime('%B, %Y')}: ${total_spent:.2f}")

def view_category_summary(category):
    total_spent = 0
    for expense_list in expenses.values():
        for expense in expense_list:
            if expense['category'].lower() == category.lower():
                total_spent += float(expense['amount'])
    print(f"Total expenses for {category.capitalize()}: ${total_spent:.2f}")

def main():
    load_expenses()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = input("Enter the amount spent: ")
            description = input("Enter a brief description: ")
            category = input("Enter the category: ")
            add_expense(amount, description, category)
            save_expenses()
        elif choice == '2':
            month = int(input("Enter the month (1-12): "))
            year = int(input("Enter the year: "))
            view_monthly_summary(month, year)
        elif choice == '3':
            category = input("Enter the category: ")
            view_category_summary(category)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
