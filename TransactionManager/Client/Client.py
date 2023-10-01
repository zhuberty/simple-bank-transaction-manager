import os
import tkinter as tk
from ..utils import get_filepath


class PageAdmin(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="This is the PageAdmin")
        label.pack(pady=10)
        self.check_directories_btn = tk.Button(
            self,
            text="Check Directories",
            command=lambda: self.check_directories(),
        )
        self.check_directories_btn.pack()
        self.errors = []

        # a read-only text window for displaying debug info
        self.debug_window = tk.Text(self, height=10, width=80)

    def check_directories(self):
        # relative_paths_to_check = [
        #     "../user_data",
        # ]
        # for relative_path in relative_paths_to_check:
        #     actual_path = os.path.join(get_cwd(__file__), relative_path)
        #     if not os.path.exists(actual_path):
        #         self.errors.append(FileNotFoundError(
        #             f"Path {actual_path} does not exist. Please create this directory and try again."
        #         ))
        # for error in self.errors:
        #     raise error
        pass


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="This is the MainPage")
        label.pack(pady=10)
        button = tk.Button(
            self,
            text="Go to PageAdmin",
            command=lambda: controller.show_frame(PageAdmin),
        )
        button.pack()


class Client(tk.Tk):
    def __init__(self, home_dir):
        super().__init__()
        self.home_dir = get_filepath(__file__, home_dir)
        if not os.path.exists(self.home_dir):
            self.create_home_dir()

        self.title("Transaction Manager")
        self.geometry("800x600+100+100")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (PageAdmin, MainPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        for frame in self.frames.values():
            frame.is_active = False  # Set is_active to False for all frames
        frame = self.frames[cont]
        frame.tkraise()
        frame.is_active = True  # Set is_active to True for the displayed frame

    def create_home_dir(self):
        os.mkdir(self.home_dir)

    def delete_home_dir(self):
        os.rmdir(self.home_dir)