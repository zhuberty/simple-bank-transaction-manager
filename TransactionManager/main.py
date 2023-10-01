import os
import logging
from .utils import get_calling_file_dir
from .Client import Client

logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO"))

ACCOUNTS_DIRECTORY = os.path.join(get_calling_file_dir(__file__), "../tests/test_data/accounts/Test Bank Account Name/statements")

def main():
    client = Client.Client()
    client.mainloop()

if __name__ == "__main__":
    main()