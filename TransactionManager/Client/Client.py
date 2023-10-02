import os
import tkinter as tk
from ..utils import get_dirpath, path_exists


class PageAdmin(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.MAX_CONOLE_LINES = 200
        self.errors = []
        self.configure_check_dirs_btn()
        self.current_console_length = 0
        self.configure_console(height=10, width=80)



    def configure_check_dirs_btn(self):
        self.check_directories_btn = tk.Button(
            self,
            text="Check Directories",
            command=lambda: self.check_directories(),
        )
        self.check_directories_btn.grid(row=1, column=0, columnspan=2)

    def configure_console(self, height, width):
        self.console = tk.Text(self, height=height, width=width, bg="black", fg="white")
        self.console.config(state="disabled")
        self.console.grid(row=2, column=0, sticky="nsew")
        self.configure_console_scrollbar()
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.log_message("Initialized application.")

    def configure_console_scrollbar(self):
        self.console_scrollbar = tk.Scrollbar(self, command=self.console.yview)
        self.console.config(yscrollcommand=self.console_scrollbar.set)
        self.console_scrollbar.grid(row=2, column=1, sticky="ns")

    def log_message(self, message):
        self.console.config(state="normal")
        self.console.insert(tk.END, message + "\n")
        self.console.see(tk.END)
        self.current_console_length += 1
        self.handle_console_buffer()
        self.console.config(state="disabled")

    def handle_console_buffer(self):
        if self.current_console_length > self.MAX_CONOLE_LINES:
            self.delete_first_console_line()

    def clear_console(self):
        self.console.config(state="normal")
        self.console.delete("1.0", tk.END)
        self.console.config(state="disabled")
        self.current_console_length = 0

    def get_console_length(self):
        return self.current_console_length

    def delete_first_console_line(self):
        self.console.delete("1.0", "2.0")
        self.current_console_length -= 1

    def configure_directories(self):
        self.log_message("Configuring directories...")
        if not self.check_main_dir_exists():
            self.create_main_dir()

    def check_main_dir_exists(self):
        self.log_message("Checking for Main directory...")
        main_dir_exists = path_exists(self.controller.main_dir)
        if not main_dir_exists:
            self.log_message("Main directory does not exist.")
        else:
            self.log_message("Main directory exists.")
        return main_dir_exists
    
    def create_main_dir(self):
        if not self.check_main_dir_exists():
            self.log_message("Creating Main directory...")
            os.mkdir(self.controller.main_dir)
            self.log_message("Main directory created.")

    def delete_main_dir(self):
        if self.check_main_dir_exists():
            self.log_message("Deleting Main directory...")
            os.rmdir(self.controller.main_dir)
            self.log_message("Main directory deleted.")


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
    def __init__(self, main_dir):
        super().__init__()
        self.main_dir = get_dirpath(__file__, main_dir)

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
