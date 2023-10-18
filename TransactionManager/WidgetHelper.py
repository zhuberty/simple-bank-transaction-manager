from tkinter.ttk import Button, Scrollbar


class WidgetHelper:
    @staticmethod
    def create_button(parent, text, command, row, column, sticky=""):
        button = Button(parent, text=text, command=command)
        button.grid(row=row, column=column, sticky=sticky)
        return button
    
    @staticmethod
    def create_scrollbar(parent, command, row, column, sticky=""):
        scrollbar = Scrollbar(parent, command=command)
        scrollbar.grid(row=row, column=column, sticky=sticky)
        return scrollbar
    
    @staticmethod
    def configure_grid(parent, rows, columns):
        for row in range(rows):
            parent.grid_rowconfigure(row, weight=1)
        for column in range(columns):
            parent.grid_columnconfigure(column, weight=1)