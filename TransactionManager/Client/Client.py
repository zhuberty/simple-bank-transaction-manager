import os
import tkinter as tk
from .FrameAdmin import FrameAdmin
from .FrameMain import FrameMain
from ..utils import get_dirpath


class Client(tk.Tk):
    def __init__(self, main_dir):
        super().__init__()
        self.main_dir = get_dirpath(__file__, main_dir)
        self.accounts_dir = os.path.join(self.main_dir, "accounts")

        self.title("Transaction Manager")
        self.geometry("800x600+100+100")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {
            "admin": FrameAdmin(container, self),
            "main": FrameMain(container, self),
        }

        self.show_frame("admin")

    def get_showing_frame(self):
        return self.showing_frame
    
    def get_frame(self, frame_name: str) -> tk.Frame:
        return self.frames[frame_name]

    def show_frame(self, frame_name: str):
        self.showing_frame = self.get_frame(frame_name)
        self.showing_frame.tkraise()