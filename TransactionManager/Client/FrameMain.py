import tkinter as tk
from .FrameAdmin import FrameAdmin


class FrameMain(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.grid(row=0, column=0, sticky="nsew")
        label = tk.Label(self, text="This is the FrameMain")
        label.pack(pady=10)
        button = tk.Button(
            self,
            text="Go to FrameAdmin",
            command=lambda: controller.show_frame("admin"),
        )
        button.pack()