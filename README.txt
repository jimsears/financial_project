Financial Transactions Tracker
Jim Sears / June 2025

This is a simple Python-based financial tracking program that lets you manage, analyze, and report your income and expenses through a terminal interface.

Features

- Load transactions from a CSV file
- Add, view, update, and delete transactions
- Analyze total income, expenses, and net balance
- Generate a detailed financial report saved as report.txt
- Save updated transactions back to financial_transactions.csv

How to Run the Program

Requirements
- Python 3.x (preferably Python 3.8 or later)

Files
Make sure you have the following files in the same directory:

- main.py – the main script you’ll run
- finance_functions.py – where all the core functionality lives
- financial_transactions.csv – your starting data file (you can start with an empty file with just the headers)
- report.txt – this will be created when you generate a report

Running the Program

1. Open a terminal or command prompt.
2. Navigate to the folder containing the project files.
3. Run the program using:

   python main.py

4. Use the on-screen menu to:
   - Load transactions (option 1)
   - Add new ones
   - Edit or delete existing ones
   - Analyze your finances
   - Save your changes
   - Generate a report file

Example Flow

1. Load existing transactions with option 1.
2. View or add transactions using options 2 and 3.
3. Make updates or delete entries as needed with options 4 and 5.
4. Use option 6 to analyze your financial overview.
5. Save changes to your CSV file using option 9.
6. Generate a report with option 8 (this creates a report.txt file in the same directory).

Notes

- The program expects dates in YYYY-MM-DD format.
- Amounts should be entered as numbers (positive for income, negative for expenses).
- If financial_transactions.csv doesn't exist, the program will notify you and start with an empty list.
- You can open financial_transactions.csv in Excel or any spreadsheet app to view or edit manually (just make sure not to remove headers).


