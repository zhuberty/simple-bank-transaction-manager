import os
import logging
import Client

logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO"))

ACCOUNTS_DIRECTORY = os.path.join(get_calling_file_dir(__file__), "/../tests/test_data/accounts/")

def main():
    client = Client()

if __name__ == "__main__":
    main()