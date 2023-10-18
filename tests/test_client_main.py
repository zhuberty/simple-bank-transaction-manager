import os
from time import sleep
from tkinter import *
from tkinter.ttk import *
import pandas as pd
from TransactionManager.Client import Client
from TransactionManager.FileHelper import FileHelper

class TestClientFrameMain:
    test_main_dir = "test_user_data_TestClientFrameMain"
    client = Client(test_main_dir)
    client.update_idletasks()
    page = client.main_frame
    mock_transactions_filepath = os.path.join(FileHelper.get_cwd(__file__), "test_data/accounts/Test Bank Account Name/statements/mock_bank_statement.csv")
    mock_transactions_df = pd.read_csv(mock_transactions_filepath)

    def test_view_transactions_from_file(self):
        self.page.transaction_viewer_frame.view_transactions_from_file(self.mock_transactions_filepath)
        # assert self.page.transaction_viewer_frame.transactions_viewer.get_children() == list(range(len(self.mock_transactions_df.index)))

