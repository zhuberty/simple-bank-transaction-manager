import os
from time import sleep
from tkinter import *
from tkinter.ttk import *
import pandas as pd
from TransactionManager.Client import Client
from TransactionManager.PageAdmin import PageAdmin
from TransactionManager.PageHome import PageHome
from TransactionManager.FileHelper import FileHelper

class TestClientPageHome:
    test_main_dir = "test_user_data"
    client = Client(test_main_dir)
    client.init_pages(PageAdmin(client.container, client), PageHome(client.container, client))
    client.update_idletasks()
    page = client.page_home
    mock_transactions_filepath = os.path.join(FileHelper.get_cwd(__file__), "test_data/accounts/Test Bank Account Name/statements/mock_bank_statement.csv")
    mock_transactions_df = pd.read_csv(mock_transactions_filepath)

    def test_view_transactions_from_file(self):
        self.page.transaction_viewer_frame.view_transactions_from_file(self.mock_transactions_filepath)
        # assert self.page.transaction_viewer_frame.transactions_viewer.get_children() == list(range(len(self.mock_transactions_df.index)))

