import pytest
from time import sleep
from TransactionManager.Client import Client
from TransactionManager.utils import path_exists


@pytest.mark.order(1)
class TestClientMainPage:
    test_home_dir = "test_user_data_TestClientMainPage"
    client = Client.Client(test_home_dir)
    client.update_idletasks()
    
    def test_check_home_dir(self):
        assert self.client.home_dir is not None


    def test_geometry_correct(self):
        assert self.client.geometry() == "800x600+100+100"

    def test_title_set(self):
        assert self.client.title() == "Transaction Manager"

    def test_frames_created(self):
        assert self.client.frames != {}

    def test_frames_correct(self):
        assert self.client.frames.keys() == {Client.PageAdmin, Client.MainPage}

    def test_show_frame(self):
        self.client.show_frame(Client.MainPage)
        # make sure other frames aren't active
        for frame in self.client.frames.values():
            if frame is not self.client.frames[Client.MainPage]:
                assert not frame.is_active

    @pytest.mark.order(1)
    def test_check_home_dir_exists(self):
        assert path_exists(self.client.home_dir)
    
    @pytest.mark.order(2)
    def test_delete_home_dir(self):
        self.client.delete_home_dir()
        assert not path_exists(self.client.home_dir)


class TestClientAdminPage:
    test_home_dir = "test_user_data_TestClientAdminPage"
    client = Client.Client(test_home_dir)
    client.update_idletasks()

    def test_show_page(self):
        self.client.show_frame(Client.PageAdmin)
        assert self.client.frames[Client.PageAdmin].is_active
        # make sure other frames aren't active
        for frame in self.client.frames.values():
            if frame is not self.client.frames[Client.PageAdmin]:
                assert not frame.is_active

    def test_check_directories_btn(self):
        page = self.client.frames[Client.PageAdmin]
        assert page.check_directories_btn is not None
        assert page.check_directories_btn["text"] == "Check Directories"
    
    def test_init_debug_window(self):
        page = self.client.frames[Client.PageAdmin]
        assert page.debug_window.winfo_viewable()
        assert page.debug_window["height"] == 10
        assert page.debug_window["width"] == 80

    @pytest.mark.order(1)
    def test_check_home_dir_exists(self):
        assert path_exists(self.client.home_dir)

    @pytest.mark.order(2)
    def test_delete_home_dir(self):
        self.client.delete_home_dir()
        assert not path_exists(self.client.home_dir)