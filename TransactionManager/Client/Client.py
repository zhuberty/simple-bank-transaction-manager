import os
import tkinter as tk
from ..utils import get_filepath


class PageAdmin(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.MAX_CONOLE_LINES = 200
        self.errors = []
        label = tk.Label(self, text="This is the PageAdmin")
        label.pack(pady=10)
        self.check_directories_btn = tk.Button(
            self,
            text="Check Directories",
            command=lambda: self.check_directories(),
        )
        self.check_directories_btn.pack()
        self.current_console_length = 0
        self.configure_console(height=10, width=80)

    def configure_console(self, height, width):
        self.console = tk.Text(self, height=height, width=width, bg="black", fg="white")
        self.console.config(state="disabled")
        self.console.pack()
        self.log_message("Initialized application.")

    def log_message(self, message):
        self.console.config(state="normal")
        self.console.insert(tk.END, message + '\n')
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

    def check_directories(self):
        self.log_message("Checking directories...")


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