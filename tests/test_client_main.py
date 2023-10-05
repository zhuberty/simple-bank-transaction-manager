import os
from time import sleep
import tkinter as tk
import pandas as pd
from TransactionManager.utils import get_cwd
from TransactionManager.Client import Client

class TestClientClientFrameMain:
    test_main_dir = "test_user_data_TestClientClientFrameMain"
    client = Client(test_main_dir)
    client.update_idletasks()
    page = client.frames["main"]
    mock_transactions_filepath = os.path.join(get_cwd(__file__), "test_data/accounts/Test Bank Account Name/statements/mock_bank_statement.csv")
    mock_transactions_df = pd.read_csv(mock_transactions_filepath)

    def test_init_frame(self):
        assert self.page.winfo_viewable()

    def test_admin_btn_exists(self):
        assert self.page.admin_btn.winfo_viewable()

    def test_import_file_btn_exists(self):
        assert self.page.import_file_btn.winfo_viewable()

    def test_import_file_dialog(self):
        self.page.import_file_btn.invoke()
        import_file_window = self.page.winfo_children()[-1]
        assert import_file_window.title() == "Import File"
        assert import_file_window.winfo_children()[0].cget("text") == "Select File"
        import_file_window.destroy()

    def test_import_file_dialog_callback(self):
        self.page.import_file_btn.invoke()
        import_file_window = self.page.winfo_children()[-1]
        self.client.frames["admin"].clear_console()
        self.page.open_file_dialog_callback("test_file.csv", import_file_window)
        assert self.client.frames["admin"].console.get("1.0", "1.end") == "Importing file: test_file.csv"
        self.client.frames["admin"].clear_console()
        self.page.open_file_dialog_callback("test_file.txt", import_file_window)
        assert self.client.frames["admin"].console.get("1.0", "1.end") == "Error: File must be a csv file"

    def test_transactions_viewer_exists(self):
        assert self.page.transactions_viewer.winfo_viewable()

    def test_display_transactions(self):
        self.page.display_transactions(self.mock_transactions_df)
        self.client.update_idletasks()
        assert self.page.transactions_viewer.get("1.0", "1.end")
