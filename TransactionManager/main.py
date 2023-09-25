from .csv_reader import read_csv
from .categorizer import categorize
from .report_generator import generate_report
from .utils import get_calling_file_dir

ACCOUNTS_DIRECTORY = get_calling_file_dir(__file__) + "/../tests/test_data/accounts/"
DEFAULT_CSV_FILE = "mock_bank_statement.csv"

def main():
    file_path = CSV_DIRECTORY + DEFAULT_CSV_FILE
    transactions = read_csv(file_path)
    
    for transaction in transactions:
        categorize(transaction)
    
    report = generate_report(transactions)
    for category, total in report.items():
        print(f"{category}: {total:.2f}")

if __name__ == "__main__":
    main()
