import tkinter as tk
from TransactionManager.Client import Client

class TestClientFrameMain:
    test_main_dir = "test_user_data_TestClientFrameMain"
    client = Client.Client(test_main_dir)
    client.update_idletasks()
    page = client.frames["main"]

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
        # make sure file dialog closes
        import_file_window.destroy()

    def test_import_file_dialog_callback(self):
        self.page.import_file_btn.invoke()
        import_file_window = self.page.winfo_children()[-1]
        self.client.frames["admin"].clear_console()
        self.page.open_file_dialog_callback("test_file.csv", import_file_window)
        assert self.client.frames["admin"].console.get("1.0", "1.end") == "Importing file: test_file.csv"
        # assert throws error if the file is not a csv file
        self.client.frames["admin"].clear_console()
        self.page.open_file_dialog_callback("test_file.txt", import_file_window)
        assert self.client.frames["admin"].console.get("1.0", "1.end") == "Error: File must be a csv file"