import os
from tkinter import *
from tkinter.ttk import *
from .FileHelper import FileHelper
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .PageAdmin import PageAdmin
    from .PageHome import PageHome

class Client(Tk):
    def __init__(self, main_dir):
        super().__init__()
        self.main_dir = FileHelper.get_dirpath(__file__, main_dir)
        self.statements_dir = os.path.join(self.main_dir, "accounts", "statements")
        self.title("Simple Bank Transaction Manager")
        self.configure_window()
        self.configure_grid()
        self.container = self.configure_container()
        self.page_admin: "PageAdmin" = None
        self.page_home: "PageHome" = None

    def configure_window(self):
        window_width = 1200
        window_height = 800
        # center the window on the screen
        x = self.winfo_screenwidth() / 2 - window_width / 2
        y = self.winfo_screenheight() / 2 - window_height / 2
        self.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))

    def configure_grid(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def configure_container(self) -> Frame:
        container = Frame(self)
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        return container

