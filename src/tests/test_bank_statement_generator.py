import csv
import os
from .utils.create_mock_bank_statement import generate_bank_statement, write_to_csv  # Assuming your original code is in a file named "bank_statement_generator.py"

def test_generate_bank_statement_num_entries():
    num_entries = 500
    data = generate_bank_statement(num_entries)
    assert len(data) == num_entries

def test_generate_bank_statement_chk_ref():
    data = generate_bank_statement(1000)
    missing_chk_ref = sum(1 for entry in data if not entry[1])
    # It won't be exact due to randomness, but should be roughly 60%.
    assert 550 < missing_chk_ref < 650

def test_generate_bank_statement_debit_credit():
    data = generate_bank_statement(1000)
    debits = sum(1 for entry in data if entry[2])
    credits = sum(1 for entry in data if entry[3])
    assert debits + credits == 1000  # Make sure each entry has a debit or credit.

def test_write_to_csv():
    data = generate_bank_statement(10)
    filename = "test_mock_bank_statement_remove.csv"
    write_to_csv(filename, data)

    # Check if file exists
    assert os.path.exists(filename)
    
    # Clean up after test
    os.remove(filename)

def test_write_to_csv_no_overwrite():
    data = generate_bank_statement(10)
    filename = "./src/tests/test_data/test_mock_bank_statement_remove.csv"
    write_to_csv(filename, data)

    # Create a dummy entry
    dummy_entry = generate_bank_statement(1)

    # Attempt to write the dummy entry to the same file
    write_to_csv(filename, dummy_entry)

    # Check if the file contains only the original 10 entries and not the dummy entry
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        assert sum(1 for row in reader) == 11  # 10 entries + 1 header
    
    # Clean up after test
    os.remove(filename)