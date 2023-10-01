import os
import logging
from .utils import get_cwd
from .Client import Client

logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO"))

ACCOUNTS_DIRECTORY = os.path.join(get_cwd(__file__), "../tests/test_data/accounts/Test Bank Account Name/statements")

def main():
    client = Client.Client()
    client.mainloop()

if __name__ == "__main__":
    main()