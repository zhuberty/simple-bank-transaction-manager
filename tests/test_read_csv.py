import os
from TransactionManager.utils import get_calling_file_dir
from TransactionManager.csv_reader import read_csv

def test_read_csv():
    # get this file's directrory path
    # get the full path to the file
    filepath = os.path.join(get_calling_file_dir(__file__), "test_data/accounts/Test Bank Account Name/statements/mock_bank_statement.csv")
    transactions = read_csv(filepath)
    assert len(transactions) == 1000
    first_transaction = transactions[0]
    assert first_transaction.account == "45253123"
    assert first_transaction.amount == 491.00
