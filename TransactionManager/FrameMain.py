from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from .TransactionViewer import TransactionViewer
from .FileHelper import FileHelper


class FrameMain(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure_grid()
        self.configure_admin_btn()
        self.configure_import_file_btn()

        self.transaction_viewer_frame = TransactionViewer(self)

    def configure_grid(self):
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.btn_container = Frame(self)
        self.btn_container.grid(row=0, column=0, sticky="nsew")
        self.btn_container.grid_columnconfigure(0, weight=1)
        self.btn_container.grid_columnconfigure(1, weight=1)

    def configure_admin_btn(self):
        self.admin_btn = Button(
            self.btn_container,
            text="Go to Admin",
            command=lambda: self.controller.show_frame("admin"),
        )
        self.admin_btn.grid(row=0, column=0, sticky="ew")
    
    def configure_import_file_btn(self):
        self.import_file_btn = Button(
            self.btn_container,
            text="Import File",
            command=self.import_file_btn_event,
        )
        self.import_file_btn.grid(row=0, column=1, sticky="ew")

    def import_file_btn_event(self):
        dialog_result = FileHelper.open_file_dialog("Select CSV File to Import")
        if FileHelper.is_valid_file(dialog_result):
            self.controller.admin_frame.console.log_message("Importing file: " + dialog_result)
            FileHelper.copy_file_to_folder(dialog_result, self.controller.statements_dir)
        else:
            self.controller.admin_frame.console.log_message("Error: File must be a csv, xls, or xlsx file.")

    def open_file_dialog(self, import_file_window):
        dialog_result = FileHelper.open_file_dialog("Select CSV File to Import")
        self.open_file_dialog_callback(dialog_result, import_file_window)

    def open_file_dialog_callback(self, dialog_result, import_file_window):
        if FileHelper.is_valid_csv_file(dialog_result):
            self.controller.admin_frame.log_message("Importing file: " + dialog_result)
        else:
            self.controller.admin_frame.log_message("Error: File must be a csv file")
        import_file_window.destroy()