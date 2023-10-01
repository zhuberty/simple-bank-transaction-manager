import tkinter as tk
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
    
    @pytest.mark.order(99)
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
    
    def test_init_console(self):
        page = self.client.frames[Client.PageAdmin]
        assert page.console.winfo_viewable()
        assert page.console["height"] == 10
        assert page.console["width"] == 80
        # make sure the debug window is read-only
        assert page.console["state"] == "disabled"

    @pytest.mark.order(1)
    def test_check_home_dir_exists(self):
        assert path_exists(self.client.home_dir)

    @pytest.mark.order(99)
    def test_delete_home_dir(self):
        self.client.delete_home_dir()
        assert not path_exists(self.client.home_dir)

    def test_clear_console(self):
        page = self.client.frames[Client.PageAdmin]
        page.clear_console()
        assert page.console.get("1.0", "1.end") == ""
        page.log_message("Test message.")
        assert page.console.get("1.0", "1.end") == "Test message."

    def test_log_message(self):
        page = self.client.frames[Client.PageAdmin]
        page.clear_console()
        page.log_message("Test message.")
        assert "Test message." in page.console.get("1.0", tk.END)

    def test_get_console_length(self):
        page = self.client.frames[Client.PageAdmin]
        page.clear_console()
        assert page.get_console_length() == 0
        page.log_message("Test message.")
        assert page.get_console_length() == 1
        page.log_message("Test message.")
        assert page.get_console_length() == 2

    @pytest.mark.order(1)
    def test_handle_console_buffer(self):
        page = self.client.frames[Client.PageAdmin]
        page.MAX_CONOLE_LINES = 2
        page.clear_console()
        page.log_message("Test message 1.")
        page.log_message("Test message 2.")
        page.log_message("Test message 3.")
        assert page.console.get("1.0", "1.end") == "Test message 2."
        assert page.console.get("2.0", "2.end") == "Test message 3."
        assert page.console.get("3.0", "3.end") == ""