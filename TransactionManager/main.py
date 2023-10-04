from .utils import get_cwd
from .Client import Client

def main(testing=False):
    if testing:
        test_client = Client(main_dir="test_user_data")
        test_client.get_frame("admin").delete_main_dir()
    else:
        client = Client(main_dir="user_data")
        client.mainloop()

if __name__ == "__main__":
    main()