import os
import tkinter as tk
from .FrameAdmin import FrameAdmin
from .FrameMain import FrameMain
from .utils import get_dirpath


class Client(tk.Tk):
    def __init__(self, main_dir):
        super().__init__()
        self.main_dir = get_dirpath(__file__, main_dir)
        self.accounts_dir = os.path.join(self.main_dir, "accounts")

        self.title("Transaction Manager")
        # center the window on the screen
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
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        return container

    def configure_frames(self):
        self.frames = {}
        self.showing_frame = None
        self.frames = {
            "admin": FrameAdmin(self.container, self),
            "main": FrameMain(self.container, self),
        }

    def get_showing_frame(self):
        return self.showing_frame
    
    def get_frame(self, frame_name: str) -> tk.Frame:
        return self.frames[frame_name]

    def show_frame(self, frame_name: str):
        self.showing_frame = self.get_frame(frame_name)
        self.showing_frame.tkraise()