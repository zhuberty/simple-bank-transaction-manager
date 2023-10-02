import tkinter as tk
import pytest
from time import sleep
from TransactionManager.Client import Client
from TransactionManager.utils import path_exists, list_dirs


@pytest.mark.order(1)
class TestClientFrameMain:
    test_main_dir = "test_user_data_TestClientFrameMain"
    client = Client.Client(test_main_dir)
    client.update_idletasks()
    
    def test_check_main_dir(self):
        assert self.client.main_dir is not None


    def test_geometry_correct(self):
        assert self.client.geometry() == "800x600+100+100"

    def test_title_set(self):
        assert self.client.title() == "Transaction Manager"

    def test_frames_created(self):
        assert self.client.frames != {}

    def test_frames_correct(self):
        assert self.client.frames.keys() == {"admin", "main"}


class TestClientAdminPage:
    test_main_dir = "test_user_data_TestClientAdminPage"
    client = Client.Client(test_main_dir)
    client.update_idletasks()

    def test_check_directories_btn(self):
        page = self.client.frames["admin"]
        assert page.check_directories_btn is not None
        assert page.check_directories_btn["text"] == "Check Directories"
    
    def test_init_console(self):
        page = self.client.frames["admin"]
        assert page.console.winfo_viewable()
        assert page.console["height"] == 10
        assert page.console["width"] == 80
        # make sure the debug window is read-only
        assert page.console["state"] == "disabled"

    def test_clear_console(self):
        page = self.client.frames["admin"]
        page.clear_console()
        assert page.console.get("1.0", "1.end") == ""
        page.log_message("Test message.")
        assert page.console.get("1.0", "1.end") == "Test message."

    def test_log_message(self):
        page = self.client.frames["admin"]
        page.clear_console()
        page.log_message("Test message.")
        assert "Test message." in page.console.get("1.0", tk.END)

    def test_get_console_length(self):
        page = self.client.frames["admin"]
        page.clear_console()
        assert page.get_console_length() == 0
        page.log_message("Test message.")
        assert page.get_console_length() == 1
        page.log_message("Test message.")
        assert page.get_console_length() == 2

    def test_handle_console_buffer(self):
        page = self.client.frames["admin"]
        page.MAX_CONOLE_LINES = 2
        page.clear_console()
        page.log_message("Test message 1.")
        page.log_message("Test message 2.")
        page.log_message("Test message 3.")
        assert page.console.get("1.0", "1.end") == "Test message 2."
        assert page.console.get("2.0", "2.end") == "Test message 3."
        assert page.console.get("3.0", "3.end") == ""

    def test_check_console_scrollbar_height(self):
        page = self.client.frames["admin"]
        assert page.console_scrollbar.winfo_height() == page.console.winfo_height()

    @pytest.mark.order(1)
    def test_check_main_dir_exists(self):
        assert path_exists(self.client.main_dir)


    @pytest.mark.order(2)
    def test_check_main_dir_exists(self):
        page = self.client.frames["admin"]
        page.clear_console()
        page.check_main_dir_exists()
        assert "Checking for Main directory..." in page.console.get("1.0", tk.END)

    @pytest.mark.order(3)
    def test_create_main_dir(self):
        page = self.client.frames["admin"]
        page.delete_main_dir()
        page.clear_console()
        page.create_main_dir()
        assert "Creating Main directory..." in page.console.get("1.0", tk.END)
        assert path_exists(self.client.main_dir)
        assert "Main directory created." in page.console.get("2.0", tk.END)
        page.clear_console()
        with pytest.raises(FileExistsError):
            page.create_main_dir()

    @pytest.mark.order(4)
    def test_configure_directories(self):
        page = self.client.frames["admin"]
        page.delete_main_dir()
        page.clear_console()
        page.configure_directories()
        assert page.console.get("1.0", "1.end") == "Configuring directories..."
        assert page.console.get("2.0", "2.end") == "Checking for Main directory..."
        assert page.console.get("3.0", "3.end") == "Main directory does not exist."
        assert page.console.get("4.0", "4.end") == "Creating Main directory..."
        assert page.console.get("5.0", "5.end") == "Main directory created."

    @pytest.mark.order(5)
    def test_delete_main_dir(self):
        page = self.client.frames["admin"]
        page.configure_directories()
        page.clear_console()
        page.delete_main_dir()
        assert not path_exists(self.client.main_dir)
        assert "Deleting Main directory..." in page.console.get("1.0", tk.END)
        assert "Main directory deleted." in page.console.get("2.0", tk.END)
