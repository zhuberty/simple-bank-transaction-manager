from .Client import Client
from .FileHelper import FileHelper

def main(testing=False):
    if testing:
        test_client = Client(main_dir="test_user_data")
    else:
        client = Client(main_dir="user_data")
        client.mainloop()

if __name__ == "__main__":
    main()