# Import specific functions from finance_functions custom module
from finance_functions import (
    load_transactions,
    add_transaction,
    view_transactions,
    update_transaction,
    delete_transaction,
    analyze_finances,
    save_transactions,
    generate_report,
    is_valid_date
)

# Define the main function that runs the application
def main():
    transactions = []
    while True:
        print("\nSmart Personal Finance Analyzer")
        # rest of your menu...
        print("\nSmart Personal Finance Analyzer")
        print("1. Load Transactions")
        print("2. Add Transaction")
        print("3. View Transactions")
        print("4. Update Transaction")
        print("5. Delete Transaction")
        print("6. Analyze Finances")
        print("7. Save Transactions")
        print("8. Generate Report")
        print("9. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            transactions = load_transactions('financial_transactions.csv')
        elif choice == '2':
            add_transaction(transactions)
        elif choice == '3':
            view_transactions(transactions)
        elif choice == '4':
            update_transaction(transactions)
        elif choice == '5':
            delete_transaction(transactions)
        elif choice == '6':
            if transactions:
                analyze_finances(transactions)
            else:
                print("No transactions loaded. Please load transactions first.")
        elif choice == '7':
            filename = input("Enter filename to save transactions (e.g., financial_transactions.csv): ")
            save_transactions(transactions, filename)
        elif choice == '8':
            generate_report(transactions)
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select a number between 1 and 9.")


# Check if this file is being run directly (not imported), then run main()
if __name__ == "__main__":
    main()