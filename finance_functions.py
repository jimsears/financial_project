import csv
from datetime import datetime

def is_valid_date(date_str):
    """
    Check if the given string is a valid date in YYYY-MM-DD format.
    """
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def valid_date(prompt):
    """
    Prompt the user repeatedly until they enter a valid date in YYYY-MM-DD format.
    """
    while True:
        date_str = input(prompt)
        if is_valid_date(date_str):
            return date_str
        else:
            print("Invalid date format. Please enter date as YYYY-MM-DD.")

def load_transactions(filename):
    """
    Load transactions from a CSV file into a list of dictionaries.
    Converts 'amount' to float for consistency.
    Skips malformed rows with invalid date or amount, printing a warning.
    """
    transactions = []
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    # Validate date format; skip if invalid
                    if not is_valid_date(row['date']):
                        print(f"Skipping transaction with invalid date: {row}")
                        continue
                    # Convert amount to float; skip if invalid
                    row['amount'] = float(row['amount'])
                    transactions.append(row)
                except (ValueError, KeyError) as e:
                    print(f"Skipping malformed transaction row: {row} ({e})")
        print(f"{len(transactions)} transactions loaded.")
    except FileNotFoundError:
        print(f"{filename} not found. Starting with empty transaction list.")
    return transactions

def add_transaction(transactions):
    """
    Prompt the user for transaction details and add the transaction to the list.
    Keeps asking for a valid amount until entered or user cancels.
    """
    print("\nAdd New Transaction")
    date = valid_date("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")
    category = input("Enter category: ")
    while True:
        amount_input = input("Enter amount: ")
        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value or type 'cancel' to abort.")
            if amount_input.lower() == 'cancel':
                print("Transaction entry canceled.")
                return

    transaction = {
        'date': date,
        'description': description,
        'category': category,
        'amount': amount
    }
    transactions.append(transaction)
    print("Transaction added successfully.")

def view_transactions(transactions):
    """
    Display all transactions in a formatted table.
    If no transactions, display a message.
    """
    if not transactions:
        print("No transactions available.")
        return

    print("\nList of Transactions:")
    print("{:<5} {:<12} {:<20} {:<15} {:>10}".format("No.", "Date", "Description", "Category", "Amount"))
    print("-" * 75)
    for idx, transaction in enumerate(transactions, start=1):
        date = transaction.get("date", "")
        description = transaction.get("description", "")
        category = transaction.get("category", "")
        amount = transaction.get("amount", 0)
        print(f"{idx:<5} {date:<12} {description:<20} {category:<15} {amount:>10.2f}")

def update_transaction(transactions):
    """
    Allow user to select a transaction to update and edit its fields.
    Invalid amount input only cancels updating the amount, other fields still updated.
    """
    if not transactions:
        print("No transactions to update.")
        return

    # Show list of transactions for selection
    for i, t in enumerate(transactions):
        print(f"{i + 1}. Date: {t['date']}, Description: {t['description']}, Category: {t.get('category', '')}, Amount: {t['amount']}")

    try:
        index = int(input("Enter the number of the transaction to update: ")) - 1
        if index < 0 or index >= len(transactions):
            print("Invalid transaction number.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    transaction = transactions[index]

    new_date = input(f"Enter new date (YYYY-MM-DD) [{transaction['date']}]: ").strip()
    if new_date:
        if not is_valid_date(new_date):
            print("Invalid date format. Date not updated.")
        else:
            transaction['date'] = new_date

    new_description = input(f"Enter new description [{transaction['description']}]: ").strip()
    if new_description:
        transaction['description'] = new_description

    new_category = input(f"Enter new category [{transaction.get('category', '')}]: ").strip()
    if new_category:
        transaction['category'] = new_category

    new_amount = input(f"Enter new amount [{transaction['amount']}]: ").strip()
    if new_amount:
        try:
            transaction['amount'] = float(new_amount)
        except ValueError:
            print("Invalid amount. Amount not updated.")

    print("Transaction updated successfully.")

def delete_transaction(transactions):
    """
    Delete a transaction selected by the user from the list.
    Prints a friendly summary of the deleted transaction.
    """
    if not transactions:
        print("No transactions to delete.")
        return

    print("Transactions:")
    for i, transaction in enumerate(transactions, start=1):
        print(f"{i}. Date: {transaction['date']}, Description: {transaction['description']}, Category: {transaction.get('category', '')}, Amount: {transaction['amount']}")

    try:
        index = int(input("Enter the number of the transaction to delete: "))
        if 1 <= index <= len(transactions):
            removed = transactions.pop(index - 1)
            print(f"Deleted transaction: Date: {removed['date']}, Description: {removed['description']}, Amount: {removed['amount']:.2f}")
        else:
            print("Invalid transaction number.")
    except ValueError:
        print("Please enter a valid number.")

def analyze_finances(transactions):
    """
    Calculate and display total income, total expenses, and net balance.
    """
    if not transactions:
        print("No transactions to analyze.")
        return

    total_income = 0
    total_expenses = 0

    for t in transactions:
        amount = float(t['amount'])
        if amount > 0:
            total_income += amount
        else:
            total_expenses += amount

    net_balance = total_income + total_expenses

    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${abs(total_expenses):.2f}")
    print(f"Net Balance: ${net_balance:.2f}")

def save_transactions(transactions, filename='financial_transactions.csv'):
    """
    Save transactions to a CSV file.
    """
    if not transactions:
        print("No transactions to save.")
        return

    fieldnames = ['date', 'description', 'category', 'amount']
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for t in transactions:
            if isinstance(t, dict):  # this line helps skip any bad rows
                writer.writerow(t)
            else:
                print(f"Skipping invalid transaction row: {t}")

    print(f"Transactions saved to {filename}")


def generate_report(transactions):
    """Generate a text report summarizing transactions and save it to report.txt."""
    if not transactions:
        print("No transactions to generate report.")
        return

    total_income = 0.0
    total_expenses = 0.0
    category_totals = {}

    for t in transactions:
        amount = float(t['amount'])
        category = t.get('category', 'Uncategorized')

        if amount >= 0:
            total_income += amount
        else:
            total_expenses += amount

        category_totals[category] = category_totals.get(category, 0.0) + amount

    net_balance = total_income + total_expenses

    report_lines = []
    report_lines.append("----- Financial Report -----")
    report_lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append(f"Total Transactions: {len(transactions)}")
    report_lines.append(f"Total Income: ${total_income:.2f}")
    report_lines.append(f"Total Expenses: ${-total_expenses:.2f}")
    report_lines.append(f"Net Balance: ${net_balance:.2f}\n")
    report_lines.append("Transactions by Category:")

    for category, total in category_totals.items():
        report_lines.append(f"  {category}: ${total:.2f}")

    report_lines.append("\nAll Transactions:")
    for t in transactions:
        date = t['date']
        desc = t['description']
        category = t.get('category', 'Uncategorized')
        amount = float(t['amount'])
        report_lines.append(f"{date} | {desc} | {category} | ${amount:.2f}")

    report_lines.append("----------------------------")

    # Print to console
    for line in report_lines:
        print(line)

    # Write to report.txt file
    print("Writing to report.txt...")  # Test line

    with open("report.txt", "w") as file:
        file.write("\n".join(report_lines))

    print("\nReport generated and saved as report.txt")
