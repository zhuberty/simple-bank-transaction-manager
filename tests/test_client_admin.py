from tkinter import *
from tkinter.ttk import *
import pytest
from TransactionManager.Client import Client
from TransactionManager.PageAdmin import PageAdmin
from TransactionManager.PageHome import PageHome

class TestClientAdmin:
    test_main_dir = "test_user_data"
    client = Client(test_main_dir)
    client.init_pages(PageAdmin(client.container, client), PageHome(client.container, client))
    client.update_idletasks()
    page = client.page_admin
    log = client.page_admin.console.log_message

    def test_init_console(self):
        page = self.client.page_admin
        assert page.console["height"] == 10
        assert page.console["width"] == 80
        assert page.console["state"] == "disabled"

    def test_clear_console(self):
        page = self.client.page_admin
        page.console.clear_console()
        assert page.console.widget.get("1.0", "1.end") == ""
        self.log("Test message.")
        assert page.console.widget.get("1.0", "1.end") == "Test message."

    def test_log_message(self):
        page = self.client.page_admin
        page.console.clear_console()
        self.log("Test message.")
        assert "Test message." in page.console.widget.get("1.0", END)

    def test_get_console_length(self):
        page = self.client.page_admin
        page.console.clear_console()
        assert page.console.get_console_length() == 0
        self.log("Test message.")
        assert page.console.get_console_length() == 1
        self.log("Test message.")
        assert page.console.get_console_length() == 2

    def test_handle_console_buffer(self):
        page = self.client.page_admin
        page.console.MAX_CONSOLE_LINES = 2
        page.console.clear_console()
        self.log("Test message 1.")
        self.log("Test message 2.")
        self.log("Test message 3.")
        assert page.console.widget.get("1.0", "1.end") == "Test message 2."
        assert page.console.widget.get("2.0", "2.end") == "Test message 3."
        assert page.console.widget.get("3.0", "3.end") == ""

    def test_check_console_scrollbar_height(self):
        page = self.client.page_admin
        assert page.console_scrollbar.winfo_height() == page.console.widget.winfo_height()

    @pytest.mark.order(1)
    def test_init_console(self):
        page = self.client.page_admin
        assert page.console.widget["height"] == 10
        assert page.console.widget["width"] == 80
        assert page.console.widget["state"] == "disabled"

