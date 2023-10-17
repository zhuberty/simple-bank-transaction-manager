import shutil
from os.path import join, basename
from tkinter import filedialog

class FileHelper:
    @staticmethod
    def open_file_dialog(title="Select File"):
        dialog_result = filedialog.askopenfilename(
            title=title,
            filetypes=(("csv files", "*.csv"), ("Excel files", "*.xls;*.xlsx"), ("all files", "*.*"))
        )
        return dialog_result

    @staticmethod
    def is_valid_file(filepath):
        return filepath.endswith(('.csv', '.xls', '.xlsx'))

    @staticmethod
    def copy_file_to_folder(src_path, dest_folder):
        dest_path = join(dest_folder, basename(src_path))
        shutil.copy(src_path, dest_path)

    @staticmethod
    def import_to_folder(title="Select File", folder="target_folder"):
        file_path = FileHelper.open_file_dialog(title)
        if FileHelper.is_valid_file(file_path):
            FileHelper.copy_file_to_folder(file_path, folder)
            return True
        return False
