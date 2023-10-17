from tkinter import filedialog

class FileHelper:
    @staticmethod
    def open_file_dialog(title="Select File"):
        dialog_result = filedialog.askopenfilename(
            title=title,
            filetypes=(("csv files", ".csv"), ("all files", "*.*"))
        )
        return dialog_result

    @staticmethod
    def is_valid_csv_file(filepath):
        return filepath.endswith(".csv")