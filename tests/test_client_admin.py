from tkinter import *
from tkinter.ttk import *
import pytest
from TransactionManager.Client import Client
from TransactionManager.utils import path_exists


class TestClientAdmin:
    test_main_dir = "test_user_data_TestClientAdminConsole"
    client = Client(test_main_dir)
    client.update_idletasks()
    page = client.admin_frame

    def test_init_console(self):
        page = self.client.admin_frame
        assert page.console["height"] == 10
        assert page.console["width"] == 80
        # make sure the debug window is read-only
        assert page.console["state"] == "disabled"

    def test_clear_console(self):
        page = self.client.admin_frame
        page.console.clear_console()
        assert page.console.console.get("1.0", "1.end") == ""
        page.console.log_message("Test message.")
        assert page.console.console.get("1.0", "1.end") == "Test message."

    def test_log_message(self):
        page = self.client.admin_frame
        page.console.clear_console()
        page.console.log_message("Test message.")
        assert "Test message." in page.console.console.get("1.0", END)

    def test_get_console_length(self):
        page = self.client.admin_frame
        page.console.clear_console()
        assert page.console.get_console_length() == 0
        page.console.log_message("Test message.")
        assert page.console.get_console_length() == 1
        page.console.log_message("Test message.")
        assert page.console.get_console_length() == 2

    def test_handle_console_buffer(self):
        page = self.client.admin_frame
        page.console.MAX_CONSOLE_LINES = 2
        page.console.clear_console()
        page.console.log_message("Test message 1.")
        page.console.log_message("Test message 2.")
        page.console.log_message("Test message 3.")
        assert page.console.console.get("1.0", "1.end") == "Test message 2."
        assert page.console.console.get("2.0", "2.end") == "Test message 3."
        assert page.console.console.get("3.0", "3.end") == ""

    def test_check_console_scrollbar_height(self):
        page = self.client.admin_frame
        assert page.console_scrollbar.winfo_height() == page.console.console.winfo_height()

    @pytest.mark.order(1)
    def test_init_console(self):
        page = self.client.admin_frame  # Updated line
        assert page.console.console["height"] == 10
        assert page.console.console["width"] == 80
        # make sure the debug window is read-only
        assert page.console.console["state"] == "disabled"

    @pytest.mark.order(2)
    def test_create_main_dir(self):
        page = self.client.admin_frame
        page.delete_main_dir()
        page.console.clear_console()
        page.create_main_dir()
        assert page.console.console.get("1.0", "1.end") == "Creating Main directory..."
        assert path_exists(self.client.main_dir)
        assert page.console.console.get("2.0", "2.end") == "Main directory created."
        page.console.clear_console()
        with pytest.raises(FileExistsError):
            page.create_main_dir()

    @pytest.mark.order(3)
    def test_create_accounts_dir(self):
        page = self.client.admin_frame
        page.console.clear_console()
        page.create_accounts_dir()
        assert page.console.console.get("1.0", "1.end") == "Creating Accounts directory..."
        assert path_exists(page.controller.accounts_dir)
        assert page.console.console.get("2.0", "2.end") == "Accounts directory created."
        page.console.clear_console()
        with pytest.raises(FileExistsError):
            page.create_accounts_dir()

    @pytest.mark.order(4)
    def test_configure_directories(self):
        page = self.client.admin_frame
        page.delete_main_dir()
        page.console.clear_console()
        page.configure_directories()
        assert page.console.console.get("1.0", "1.end") == "Configuring directories..."
        assert page.console.console.get("2.0", "2.end") == f"Checking for directory: {self.client.main_dir}"
        assert page.console.console.get("3.0", "3.end") == "Directory does not exist."
        assert page.console.console.get("4.0", "4.end") == "Creating Main directory..."
        assert page.console.console.get("5.0", "5.end") == "Main directory created."

    @pytest.mark.order(50)
    def test_delete_main_dir(self):
        page = self.client.admin_frame
        page.configure_directories()
        page.console.clear_console()
        page.delete_main_dir()
        assert not path_exists(self.client.main_dir)
        assert "Deleting Main directory..." in page.console.console.get("1.0", END)
        assert "Main directory deleted." in page.console.console.get("2.0", END)
