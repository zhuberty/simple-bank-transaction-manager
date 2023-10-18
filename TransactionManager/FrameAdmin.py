import os
from tkinter import *
from tkinter.ttk import *
from .Console import Console
from .FileHelper import FileHelper


class FrameAdmin(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.MAX_CONOLE_LINES = 200
        self.errors = []
        self.current_console_length = 0
        self.grid(row=0, column=0, sticky="nsew")
        self.configure_grid()

        self.console = Console(self)
        self.console.grid(row=2, column=0, columnspan=4, sticky="nsew")
        self.configure_console_scrollbar()
        self.console.log_message("Initialized application.")
        
        self.configure_clear_console_btn()
        self.configure_frame_main_btn()

    def configure_console_scrollbar(self):
        self.console_scrollbar = Scrollbar(self, command=self.console.console.yview)
        self.console.console.config(yscrollcommand=self.console_scrollbar.set)
        self.console_scrollbar.grid(row=2, column=3, sticky="nse")

    def configure_grid(self):
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)

    def configure_frame_main_btn(self):
        self.frame_main_btn = Button(
            self,
            text="Home",
            command=lambda: self.controller.main_frame.tkraise(),
        )
        self.frame_main_btn.grid(row=1, column=0, sticky="ew")

    def configure_clear_console_btn(self):
        self.clear_console_btn = Button(
            self, text="Clear Console", command=lambda: self.console.clear_console()
        )
        self.clear_console_btn.grid(row=1, column=1, sticky="ew")

    def configure_console_scrollbar(self):
        self.console_scrollbar = Scrollbar(self, command=self.console.console.yview)
        self.console.console.config(yscrollcommand=self.console_scrollbar.set)
        self.console_scrollbar.grid(row=2, column=2, sticky="nse")

