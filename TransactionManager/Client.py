import os
from tkinter import *
from tkinter.ttk import *
from .FrameAdmin import FrameAdmin
from .FrameMain import FrameMain
from .utils import get_dirpath


class Client(Tk):
    def __init__(self, main_dir):
        super().__init__()
        self.main_dir = get_dirpath(__file__, main_dir)
        self.accounts_dir = os.path.join(self.main_dir, "accounts")

        self.title("Transaction Manager")
        self.configure_window()
        self.container = self.configure_container()
        self.configure_frames()
        self.show_frame("main")


    def configure_window(self):
        window_width = 1200
        window_height = 800
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # center the window on the screen
        x = screen_width / 2 - window_width / 2
        y = screen_height / 2 - window_height / 2
        self.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))

    def configure_container(self):
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        return container

    def configure_frames(self):
        self.showing_frame = None
        self.admin_frame = FrameAdmin(self.container, self)
        self.main_frame = FrameMain(self.container, self)

    def get_showing_frame(self):
        return self.showing_frame

    def get_frame(self, frame_name: str) -> Frame:
        if frame_name == "admin":
            return self.admin_frame
        elif frame_name == "main":
            return self.main_frame
        else:
            raise KeyError(f"No frame named {frame_name}")

    def show_frame(self, frame_name: str):
        self.showing_frame = self.get_frame(frame_name)
        self.showing_frame.tkraise()