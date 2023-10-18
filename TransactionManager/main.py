from .Client import Client
from .PageAdmin import PageAdmin
from .PageHome import PageHome


def create_pages(client: Client):
    PageAdmin(client.container, client)
    PageHome(client.container, client)


def main(testing=False):
    if testing:
        test_client = Client(main_dir="test_user_data")
        create_pages(test_client)
    else:
        client = Client(main_dir="user_data")
        create_pages(client)
        client.page_home.tkraise()
        client.mainloop()


if __name__ == "__main__":
    main()