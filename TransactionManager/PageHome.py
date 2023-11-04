from typing import TYPE_CHECKING
from tkinter import *
from tkinter.ttk import *
from .TransactionViewer import TransactionViewer
from .FileHelper import FileHelper
from .WidgetHelper import WidgetHelper

if TYPE_CHECKING:
    from .Client import Client


class PageHome(Frame):
    def __init__(self, parent: Frame, controller: "Client"):
        super().__init__(parent)
        self.controller = controller
        self.controller.page_home = self
        self.log = self.controller.page_admin.console.log_message
        self.configure_grid()
        self.admin_btn = WidgetHelper.create_button(self.btn_container, "Go to Admin", lambda: self.controller.page_admin.tkraise(), 0, 0, "ew")
        self.import_transactions_btn = WidgetHelper.create_button(self.btn_container, "Import File", self.import_transactions_btn_event, 0, 1, "ew")
        self.transactions_filepath = FileHelper.path(self.controller.statements_dir, "transactions.csv")
        self.transaction_viewer = TransactionViewer(self, self.transactions_filepath)
        self.init_transactions_file()
        self.transaction_viewer.display_transactions()


    def configure_grid(self):
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.btn_container = Frame(self)
        self.btn_container.grid(row=0, column=0, sticky="nsew")
        WidgetHelper.configure_grid(self.btn_container, 1, 2)

    def import_transactions_btn_event(self):
        dialog_result = FileHelper.open_file_dialog("Select CSV File to Import")
        if FileHelper.is_valid_csv(dialog_result):
            self.copy_file_to_tmp(dialog_result)
            file_name = FileHelper.get_filename(dialog_result)
            self.import_transactions(file_name)
        else:
            self.log("Error: File must be a csv, xls, or xlsx file.")

    def copy_file_to_tmp(self, dialog_result):
        self.log("Importing file: " + dialog_result)
        tmp_dir = FileHelper.path(self.controller.statements_dir, "tmp")
        FileHelper.copy_file_to_folder(dialog_result, tmp_dir)
        self.log("Copied file to tmp directory: " + tmp_dir)
        return FileHelper.path(tmp_dir, FileHelper.get_filename(dialog_result))

    def import_transactions(self, file_name):
        self.log("Importing transactions from file: " + file_name)
        filepath = FileHelper.path(self.controller.statements_dir, "tmp", file_name)
        transactions = FileHelper.read_csv(filepath)
        FileHelper.append_csv(self.transactions_filepath, transactions[1:])
        FileHelper.delete_file(filepath)
        self.transaction_viewer.display_transactions()

    def init_transactions_file(self):
        if not FileHelper.path_exists(self.transactions_filepath):
            FileHelper.create_file(self.transactions_filepath)
        if FileHelper.is_empty(self.transactions_filepath):
            FileHelper.append_csv(self.transactions_filepath, ",".join(self.transaction_viewer.get_transaction_columns()) + "\n")
