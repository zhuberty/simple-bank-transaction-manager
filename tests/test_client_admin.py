from tkinter import *
from tkinter.ttk import *
import pytest
from TransactionManager.Client import Client
from TransactionManager.FileHelper import FileHelper


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
    def test_create_app_directories(self):
        FileHelper.rmdir_recursively(self.client.main_dir)
        self.client.create_app_directories()
        assert FileHelper.path_exists(self.client.main_dir)
        assert FileHelper.path_exists(self.client.statements_dir)

    @pytest.mark.order(50)
    def test_delete_main_dir(self):
        page = self.client.admin_frame
        page.console.clear_console()
        FileHelper.rmdir_recursively(self.client.main_dir)
        assert not FileHelper.path_exists(self.client.main_dir)
