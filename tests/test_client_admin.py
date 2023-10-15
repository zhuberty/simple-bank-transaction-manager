from tkinter import *
from tkinter.ttk import *
import pytest
from TransactionManager.Client import Client
from TransactionManager.utils import path_exists


class TestClientAdmin:
    test_main_dir = "test_user_data_TestClientAdminConsole"
    client = Client(test_main_dir)
    client.update_idletasks()

    def test_init_console(self):
        page = self.client.frames["admin"]
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
        assert "Test message." in page.console.get("1.0", END)

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
        page = self.client.frames["admin"]
        page.clear_console()
        page.check_dir_exists(self.client.main_dir)
        assert page.console.get("1.0", "1.end") == f"Checking for directory: {self.client.main_dir}"
    @pytest.mark.order(2)
    def test_create_main_dir(self):
        page = self.client.frames["admin"]
        page.delete_main_dir()
        page.clear_console()
        page.create_main_dir()
        assert page.console.get("1.0", "1.end") == "Creating Main directory..."
        assert path_exists(self.client.main_dir)
        assert page.console.get("2.0", "2.end") == "Main directory created."
        page.clear_console()
        with pytest.raises(FileExistsError):
            page.create_main_dir()

    @pytest.mark.order(3)
    def test_create_accounts_dir(self):
        page = self.client.frames["admin"]
        page.clear_console()
        page.create_accounts_dir()
        assert page.console.get("1.0", "1.end") == "Creating Accounts directory..."
        assert path_exists(page.controller.accounts_dir)
        assert page.console.get("2.0", "2.end") == "Accounts directory created."
        page.clear_console()
        with pytest.raises(FileExistsError):
            page.create_accounts_dir()

    @pytest.mark.order(4)
    def test_configure_directories(self):
        page = self.client.frames["admin"]
        page.delete_main_dir()
        page.clear_console()
        page.configure_directories()
        assert page.console.get("1.0", "1.end") == "Configuring directories..."
        assert page.console.get("2.0", "2.end") == f"Checking for directory: {self.client.main_dir}"
        assert page.console.get("3.0", "3.end") == "Directory does not exist."
        assert page.console.get("4.0", "4.end") == "Creating Main directory..."
        assert page.console.get("5.0", "5.end") == "Main directory created."

    @pytest.mark.order(50)
    def test_delete_main_dir(self):
        page = self.client.frames["admin"]
        page.configure_directories()
        page.clear_console()
        page.delete_main_dir()
        assert not path_exists(self.client.main_dir)
        assert "Deleting Main directory..." in page.console.get("1.0", END)
        assert "Main directory deleted." in page.console.get("2.0", END)
