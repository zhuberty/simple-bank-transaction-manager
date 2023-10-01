from time import sleep
from TransactionManager.Client import Client


class TestClientMainPage:
    test_home_dir = "test_user_data_TestClientAdminPage"
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
        # loop over other frames and make sure they are not active
        for frame in self.client.frames.values():
            if frame is not self.client.frames[Client.MainPage]:
                assert not frame.is_active


class TestClientAdminPage:
    test_home_dir = "test_user_data_TestClientAdminPage"
    client = Client.Client(test_home_dir)
    client.update_idletasks()

    def test_show_page(self):
        self.client.show_frame(Client.PageAdmin)
        assert self.client.frames[Client.PageAdmin].is_active
        for frame in self.client.frames.values():
            if frame is not self.client.frames[Client.PageAdmin]:
                assert not frame.is_active

    def test_check_directories_btn(self):
        page = self.client.frames[Client.PageAdmin]
        assert page.check_directories_btn is not None
        assert page.check_directories_btn["text"] == "Check Directories"
        
    def test_debug_window_exists(self):
        page = self.client.frames[Client.PageAdmin]
        assert page.debug_window is not None
        assert page.debug_window["height"] == 10
        assert page.debug_window["width"] == 80
