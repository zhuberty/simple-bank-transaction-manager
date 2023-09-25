import os
import logging
from .csv_reader import read_csv
from .categorizer import categorize
from .report_generator import generate_report
from .utils import get_calling_file_dir

logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO"))

ACCOUNTS_DIRECTORY = get_calling_file_dir(__file__) + "/../tests/test_data/accounts/"

def main():
    file_path = os.path.join(ACCOUNTS_DIRECTORY, "Test Bank Account Name/statements/mock_bank_statement.csv")
    transactions = read_csv(file_path)
    
    for transaction in transactions:
        categorize(transaction)
    
    report = generate_report(transactions)
    for category, total in report.items():
        print(f"{category}: {total:.2f}")

if __name__ == "__main__":
    main()
