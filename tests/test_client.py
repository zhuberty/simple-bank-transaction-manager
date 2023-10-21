from TransactionManager.Client import Client
from TransactionManager.main import create_pages


class TestClient:
    test_main_dir = "test_user_data"
    client = Client(test_main_dir)
    create_pages(client)
    client.update_idletasks()

    def test_check_main_dir(self):
        assert self.client.main_dir is not None

    def test_title_set(self):
        assert self.client.title() == "Simple Bank Transaction Manager"

    def test_frames_created(self):
        assert self.client.page_admin is not None
        assert self.client.page_home is not None
