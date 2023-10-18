import os
from tkinter import *
from tkinter.ttk import *
from .FrameAdmin import FrameAdmin
from .FrameMain import FrameMain
from .FileHelper import FileHelper


class Client(Tk):
    def __init__(self, main_dir):
        super().__init__()
        self.main_dir = FileHelper.get_dirpath(__file__, main_dir)
        self.statements_dir = os.path.join(self.main_dir, "accounts", "statements")
        self.create_app_directories()

        self.title("Simple Bank Transaction Manager")
        self.configure_window()
        self.container = self.configure_container()
        self.admin_frame = FrameAdmin(self.container, self)
        self.main_frame = FrameMain(self.container, self)
        self.main_frame.tkraise()

    def configure_window(self):
        window_width = 1200
        window_height = 800
        # center the window on the screen
        x = self.winfo_screenwidth() / 2 - window_width / 2
        y = self.winfo_screenheight() / 2 - window_height / 2
        self.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))

    def configure_container(self):
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        return container

    def create_app_directories(self):
        FileHelper.create_dirs(self.statements_dir)