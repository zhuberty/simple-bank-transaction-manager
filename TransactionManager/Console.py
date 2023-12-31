from tkinter import Text, END

class Console:
    def __init__(self, parent, height=10, width=80):
        self.parent = parent
        self.widget = Text(self.parent, height=height, width=width, background="black", foreground="white", font=("Courier", 12))
        self.widget.config(state="disabled")
        self.current_console_length = 0
        self.MAX_CONSOLE_LINES = 200

    def log_message(self, message):
        self.widget.config(state="normal")
        self.widget.insert(END, message + "\n")
        self.widget.see(END)
        self.current_console_length += 1
        self.handle_console_buffer()
        self.widget.config(state="disabled")

    def handle_console_buffer(self):
        if self.current_console_length > self.MAX_CONSOLE_LINES:
            self.delete_first_console_line()

    def clear_console(self):
        self.widget.config(state="normal")
        self.widget.delete("1.0", END)
        self.widget.config(state="disabled")
        self.current_console_length = 0

    def delete_first_console_line(self):
        self.widget.delete("1.0", "2.0")
        self.current_console_length -= 1

    def grid(self, **kwargs):
        self.widget.grid(**kwargs)

    def get_console_length(self):
        return self.current_console_length