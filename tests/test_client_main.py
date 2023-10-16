import os
from time import sleep
from tkinter import *
from tkinter.ttk import *
import pandas as pd
from TransactionManager.utils import get_cwd
from TransactionManager.Client import Client

class TestClientFrameMain:
    test_main_dir = "test_user_data_TestClientFrameMain"
    client = Client(test_main_dir)
    client.update_idletasks()
    page = client.main_frame
    mock_transactions_filepath = os.path.join(get_cwd(__file__), "test_data/accounts/Test Bank Account Name/statements/mock_bank_statement.csv")
    mock_transactions_df = pd.read_csv(mock_transactions_filepath)

    def test_import_file_dialog(self):
        self.page.import_file_btn.invoke()
        import_file_window = self.page.winfo_children()[-1]
        assert import_file_window.title() == "Import File"
        assert import_file_window.winfo_children()[0].cget("text") == "Select File"
        import_file_window.destroy()

    def test_import_file_dialog_callback(self):
        self.page.import_file_btn.invoke()
        import_file_window = self.page.winfo_children()[-1]
        self.client.admin_frame.clear_console()
        self.page.open_file_dialog_callback("test_file.csv", import_file_window)
        assert self.client.admin_frame.console.get("1.0", "1.end") == "Importing file: test_file.csv"
        self.client.admin_frame.clear_console()
        self.page.open_file_dialog_callback("test_file.txt", import_file_window)
        assert self.client.admin_frame.console.get("1.0", "1.end") == "Error: File must be a csv file"

    def test_view_transactions_from_file(self):
        self.page.transaction_viewer_frame.view_transactions_from_file(self.mock_transactions_filepath)
        # assert self.page.transaction_viewer_frame.transactions_viewer.get_children() == list(range(len(self.mock_transactions_df.index)))

