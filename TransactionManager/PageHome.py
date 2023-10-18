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
        self.transaction_viewer_frame = TransactionViewer(self)

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
        if FileHelper.is_valid_file(dialog_result):
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
        filepath = FileHelper.path(self.controller.statements_dir, "tmp", file_name)
        self.transaction_viewer_frame.view_transactions_from_file(filepath)
        self.log("Imported transactions from file: " + filepath)