
import csv
from .transaction import Transaction

def read_csv(file_path):
    transactions = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            account, chkref, debit, credit, date, description = row
            # Calculate amount: positive for credits and negative for debits
            amount = (float(credit) if credit else 0.0) - (float(debit) if debit else 0.0)
            transactions.append(Transaction(account, chkref, amount, date, description))
    return transactions
