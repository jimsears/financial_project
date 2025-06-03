   # Import the .csv file
import csv  
   # Module to work with date and time objects
from datetime import datetime  

def load_transactions(filename='financial_transactions.csv'):
    # Create an empty list to hold all transactions as dictionaries
    transactions = []
    
    try:
        # Try to open the CSV file in read mode with UTF-8 encoding to support special characters
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            # csv.DictReader reads the CSV and maps each row into a dictionary
            reader = csv.DictReader(csvfile)
            
            # Loop over each row in the CSV file one at a time
            for row in reader:
                try:
                    # This converts the 'date' string from the CSV into a datetime object
                    # datetime.strptime parses a string based on the given format '%Y-%m-%d' (year-month-day)
                    date = datetime.strptime(row['date'], '%Y-%m-%d')
                    
                    # This converts the 'transaction_id' from string to integer
                    transaction_id = int(row['transaction_id'])
                    
                    # This converts the 'customer_id' from string to integer
                    customer_id = int(row['customer_id'])
                    
                    # THis converts the 'amount' from string to floating point number
                    amount = float(row['amount'])
                    
                    # Check if the transaction type is 'debit' (case-insensitive)
                    # If yes, multiply the amount by -1 to represent money spent (negative value)
                    if row['type'].lower() == 'debit':
                        amount = -amount
                    
                    # Build a dictionary that stores all the transaction details with proper data types
                    transaction = {
                        'transaction_id': transaction_id,  # Unique ID of transaction
                        'date': date,                      # Date object representing transaction date
                        'customer_id': customer_id,        # Customer's unique ID
                        'amount': amount,                  # Transaction amount (negative if debit)
                        'type': row['type'],               # Type of transaction as a string
                        'description': row['description'] # Additional description or notes
                    }
                    
                    # Add this transaction dictionary to our list of transaactions
                    transactions.append(transaction)
                
                except ValueError as e:
                    # If conversion fails, skip row
                    # Print a warning message with details about the problematic row and error
                    print(f"Skipping row due to data error: {row}. Error: {e}")
    
    except FileNotFoundError:
        # If the CSV file does not exist at the specified path, inform user:
        print(f"Error: The file '{filename}' was not found.")
    
    # After processing all rows, return the list containing all successfully loaded transactions
    return transactions