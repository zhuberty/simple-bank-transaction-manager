import tkinter as tk
import pandas as pd
from tkinter import filedialog
from tkintertable import TableCanvas, TableModel


class ClientFrameMain(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure_grid()
        self.transactions_table_model = TableModel()
        self.configure_admin_btn()
        self.configure_import_file_btn()
        self.configure_preview_file_btn()
        self.configure_transactions_viewer()

    def configure_grid(self):
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.btn_container = tk.Frame(self)
        self.btn_container.grid(row=0, column=0, sticky="nsew")
        self.btn_container.grid_columnconfigure(0, weight=1)
        self.btn_container.grid_columnconfigure(1, weight=1)
        self.btn_container.grid_columnconfigure(2, weight=1)
        self.transactions_container = tk.Frame(self)
        self.transactions_container.grid(row=1, column=0, sticky="nsew")
        self.transactions_container.grid_columnconfigure(0, weight=0)
        self.transactions_container.grid_columnconfigure(1, weight=1)
        self.transactions_container.grid_columnconfigure(2, weight=0)

    def configure_admin_btn(self):
        self.admin_btn = tk.Button(
            self.btn_container,
            text="Go to Admin",
            command=lambda: self.controller.show_frame("admin"),
        )
        self.admin_btn.grid(row=0, column=0, sticky="ew")

    def configure_import_file_btn(self):
        self.import_file_btn = tk.Button(
            self.btn_container,
            text="Import File",
            command=self.import_file_btn_event,
        )
        self.import_file_btn.grid(row=0, column=1, sticky="ew")
    
    def configure_preview_file_btn(self):
        self.preview_file_btn = tk.Button(
            self.btn_container,
            text="Preview File",
            command=self.preview_file_btn_event,
        )
        self.preview_file_btn.grid(row=0, column=2, sticky="ew")

    def preview_file_btn_event(self):
        # select file dialog
        dialog_result = filedialog.askopenfilename(
            title="Select CSV File to Preview",
            filetypes=(("csv files", ".csv"), ("all files", "*.*"))
        )
        self.view_transactions_from_file(dialog_result)

    def configure_transactions_viewer(self):
        # create a table to display transactions
        self.transactions_viewer = TableCanvas(
            self.transactions_container,
            self.transactions_table_model,
            read_only=False,
            cellbackgr='white',
            entrybackgr='white',
            selectedcolor='yellow',
            rowselectedcolor='yellow',
            multipleselectioncolor='yellow',
            rowheaderwidth=0,
        )

    def import_file_btn_event(self):
        import_file_window = tk.Toplevel(self)
        import_file_window.title("Import File")

        select_file_btn = tk.Button(
            import_file_window,
            text="Select File",
            command=lambda: self.open_file_dialog(import_file_window)
        )

    def open_file_dialog(self, import_file_window):
        dialog_result = filedialog.askopenfilename(
            title="Select CSV File to Import",
            filetypes=(("csv files", ".csv"), ("all files", "*.*"))
        )
        self.open_file_dialog_callback(dialog_result, import_file_window)

    def open_file_dialog_callback(self, dialog_result, import_file_window):
        if dialog_result.endswith(".csv"):
            self.controller.frames["admin"].log_message("Importing file: " + dialog_result)
        else:
            self.controller.frames["admin"].log_message("Error: File must be a csv file")
        import_file_window.destroy()

    def is_valid_csv_file(self, filepath):
        if filepath.endswith(".csv"):
            return True
        else:
            return False

    def view_transactions_from_file(self, filepath):
        if self.is_valid_csv_file(filepath):
            self.transactions_viewer.importCSV(filepath)
            self.transactions_viewer.redrawTable()
        else:
            self.controller.frames["admin"].log_message("Error: File must be a csv file")