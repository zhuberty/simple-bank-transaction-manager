import os
from TransactionManager.csv_reader import read_csv

def test_read_csv():
    # get this file's directrory path
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # get the full path to the file
    filepath = os.path.join(current_dir, "test_data/mock_bank_statement.csv")
    transactions = read_csv(filepath)
    assert len(transactions) == 1000
    first_transaction = transactions[0]
    assert first_transaction.account == "45253123"
    assert first_transaction.amount == 491.00
