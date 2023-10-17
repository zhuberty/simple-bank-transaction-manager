import os
from tkinter import *
from tkinter.ttk import *
from .Console import Console
from .utils import path_exists, rmdir_recursively


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

        self.configure_check_dirs_btn()
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
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=0)

    def configure_frame_main_btn(self):
        self.frame_main_btn = Button(
            self,
            text="Home",
            command=lambda: self.controller.show_frame("main"),
        )
        self.frame_main_btn.grid(row=1, column=0, sticky="ew")

    def configure_check_dirs_btn(self):
        self.check_directories_btn = Button(
            self,
            text="Check Directories",
            command=lambda: self.configure_directories(),
        )
        self.check_directories_btn.grid(row=1, column=1, sticky="ew")

    def configure_clear_console_btn(self):
        self.clear_console_btn = Button(
            self, text="Clear Console", command=lambda: self.console.clear_console()
        )
        self.clear_console_btn.grid(row=1, column=2, sticky="ew")

    def configure_console(self, height, width):
        self.console = Text(self, height=height, width=width, background="black", foreground="white", font=("Courier", 12))
        self.console.config(state="disabled")
        self.console.grid(
            row=2, column=0, columnspan=4, sticky="nsew"  # Change columnspan to 4
        )
        self.configure_console_scrollbar()
        self.console.log_message("Initialized application.")

    def configure_console_scrollbar(self):
        self.console_scrollbar = Scrollbar(self, command=self.console.console.yview)

        self.console.console.config(yscrollcommand=self.console_scrollbar.set)
        self.console_scrollbar.grid(row=2, column=3, sticky="nse")  # Change column to 3

    def configure_directories(self):
        self.console.log_message("Configuring directories...")
        if not self.check_dir_exists(self.controller.main_dir):
            self.create_main_dir()

        accounts_dir = os.path.join(self.controller.main_dir, "accounts")
        if not self.check_dir_exists(accounts_dir):
            self.create_accounts_dir()

        statements_dir = os.path.join(self.controller.main_dir, "accounts", "statements")
        if not self.check_dir_exists(statements_dir):
            os.mkdir(statements_dir)
            self.console.log_message("Statements directory created.")

    def check_dir_exists(self, path):
        self.console.log_message("Checking for directory: " + path)
        dir_exists = path_exists(path)
        if not dir_exists:
            self.console.log_message("Directory does not exist.")
        else:
            self.console.log_message("Directory exists.")
        return dir_exists


    def create_main_dir(self):
        self.console.log_message("Creating Main directory...")
        os.mkdir(self.controller.main_dir)
        self.console.log_message("Main directory created.")


    def delete_main_dir(self):
        self.console.log_message("Deleting Main directory...")
        # remove the main directory recursively
        if path_exists(self.controller.main_dir):
            rmdir_recursively(self.controller.main_dir)
            self.console.log_message("Main directory deleted.")
        else:
            self.console.log_message("Main directory does not exist.")

    def create_accounts_dir(self):
        self.console.log_message("Creating Accounts directory...")
        os.mkdir(os.path.join(self.controller.main_dir, "accounts"))
        self.console.log_message("Accounts directory created.")
        
