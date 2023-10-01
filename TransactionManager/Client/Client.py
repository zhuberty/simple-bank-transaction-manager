import tkinter as tk


class PageAdmin(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="This is the PageAdmin")
        label.pack(pady=10)
        button = tk.Button(
            self,
            text="Go to Main Page",
            command=lambda: controller.show_frame(MainPage),
        )
        button.pack()


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
    def __init__(self):
        super().__init__()
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
