# Import pandas library for data manipulation
import pandas as pd

# Load the CSV file from the current folder
df = pd.read_csv('financial_transactions.csv')

# Print the first few rows to see the data
print(df.head())

# Print column names to understand the dataset
print("\nColumns in the dataset:")
print(df.columns)