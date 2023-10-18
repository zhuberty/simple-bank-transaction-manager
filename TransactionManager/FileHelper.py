import os
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
        if not os.path.exists(dest_path):
            FileHelper.create_dirs(dest_folder)
        shutil.copy(src_path, dest_path)

    @staticmethod
    def create_dirs(dir_path):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    @staticmethod
    def create_file(filepath):
        open(filepath, "w+").close()

    @staticmethod
    def import_to_folder(title="Select File", folder="target_folder"):
        file_path = FileHelper.open_file_dialog(title)
        if FileHelper.is_valid_file(file_path):
            FileHelper.copy_file_to_folder(file_path, folder)
            return True
        return False

    @staticmethod
    def get_cwd(file) -> str:
        """
        file: __file__ from the calling file.
        ex. get_cwd(__file__)
        """
        return os.path.dirname(os.path.realpath(file))

    @staticmethod
    def get_dirpath(file, dir) -> str:
        """
        file: __file__ from the calling file.
        dir: the directory to get the path for.
        ex. get_dirpath(__file__, "test_data")
        """
        return os.path.join(FileHelper.get_cwd(file), dir)

    @staticmethod
    def path_exists(path):
        return os.path.exists(path)

    @staticmethod
    def list_dirs(path) -> list:
        dirs = []
        for item in os.listdir(path):
            if os.path.isdir(os.path.join(path, item)):
                dirs.append(item)
        return dirs

    @staticmethod
    def rmdir_recursively(dir_path):
        shutil.rmtree(dir_path)

    @staticmethod
    def path(*args):
        return os.path.join(*args)

