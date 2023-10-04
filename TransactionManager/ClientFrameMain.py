import tkinter as tk
from tkinter import filedialog
from .ClientFrameAdmin import ClientFrameAdmin


class ClientFrameMain(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure_grid()
        self.configure_admin_btn()
        self.configure_import_file_btn()

    def configure_grid(self):
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def configure_admin_btn(self):
        self.admin_btn = tk.Button(
            self,
            text="Go to Admin",
            command=lambda: self.controller.show_frame("admin"),
        )
        self.admin_btn.grid(row=0, column=0, sticky="new")

    def configure_import_file_btn(self):
        self.import_file_btn = tk.Button(
            self,
            text="Import File",
            command=self.import_file_btn_event,
        )
        self.import_file_btn.grid(row=0, column=1, sticky="new")

    def import_file_btn_event(self):
        import_file_window = tk.Toplevel(self)
        import_file_window.title("Import File")

        select_file_btn = tk.Button(
            import_file_window,
            text="Select File",
            command=lambda: self.open_file_dialog(import_file_window)
        )
        select_file_btn.pack(pady=20)

    def open_file_dialog(self, import_file_window):
        dialog_result = filedialog.askopenfilename()
        self.open_file_dialog_callback(dialog_result, import_file_window)

    def open_file_dialog_callback(self, dialog_result, import_file_window):
        if dialog_result.endswith(".csv"):
            self.controller.frames["admin"].log_message("Importing file: " + dialog_result)
        else:
            self.controller.frames["admin"].log_message("Error: File must be a csv file")
        import_file_window.destroy()
