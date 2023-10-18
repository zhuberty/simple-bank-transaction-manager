import os
from tkinter import *
from tkinter.ttk import *
from .Console import Console
from .WidgetHelper import WidgetHelper


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
        
        self.clear_console_btn = WidgetHelper.create_button(self, "Clear Console", lambda: self.console.clear_console(), 1, 1, "ew")
        self.frame_main_btn = WidgetHelper.create_button(self, "Home", lambda: self.controller.main_frame.tkraise(), 1, 0, "ew")

    def configure_console_scrollbar(self):
        self.console_scrollbar = Scrollbar(self, command=self.console.widget.yview)
        self.console.widget.config(yscrollcommand=self.console_scrollbar.set)
        self.console_scrollbar.grid(row=2, column=3, sticky="nse")

    def configure_grid(self):
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)

    def configure_console_scrollbar(self):
        self.console_scrollbar = WidgetHelper.create_scrollbar(self, self.console.widget.yview, 2, 2, "nse")
        self.console.widget.config(yscrollcommand=self.console_scrollbar.set)


