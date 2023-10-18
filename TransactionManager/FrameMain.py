from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from .TransactionViewer import TransactionViewer
from .FileHelper import FileHelper
from .WidgetHelper import WidgetHelper


class FrameMain(Frame):
    global log
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.log = self.controller.admin_frame.console.log_message
        self.configure_grid()
        self.admin_btn = WidgetHelper.create_button(self.btn_container, "Go to Admin", lambda: self.controller.admin_frame.tkraise(), 0, 0, "ew")
        self.import_file_btn = WidgetHelper.create_button(self.btn_container, "Import File", self.import_file_btn_event, 0, 1, "ew")
        self.transaction_viewer_frame = TransactionViewer(self)

    def configure_grid(self):
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.btn_container = Frame(self)
        self.btn_container.grid(row=0, column=0, sticky="nsew")
        WidgetHelper.configure_grid(self.btn_container, 1, 2)

    def import_file_btn_event(self):
        dialog_result = FileHelper.open_file_dialog("Select CSV File to Import")
        if FileHelper.is_valid_file(dialog_result):
            self.log("Importing file: " + dialog_result)
            FileHelper.copy_file_to_folder(dialog_result, self.controller.statements_dir)
        else:
            self.log("Error: File must be a csv, xls, or xlsx file.")
