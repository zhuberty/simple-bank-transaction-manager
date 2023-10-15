from tkinter import *
from tkinter.ttk import *

import pandas as pd


class ClientTransactionViewer(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure_grid()
        self.configure_transactions_viewer()

    def configure_grid(self):
        self.grid(row=1, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.transactions_container = Frame(self)
        self.transactions_container.grid(row=1, column=0, sticky="nsew")
        self.transactions_container.grid_columnconfigure(0, weight=0)
        self.transactions_container.grid_columnconfigure(1, weight=1)
        self.transactions_container.grid_columnconfigure(2, weight=0)

    def configure_transactions_viewer(self):
        # Create a treeview for the table
        self.transactions_viewer = Treeview(self.transactions_container)
        self.transactions_viewer.grid(row=0, column=1, sticky="nsew")
        self.transactions_viewer["columns"] = ("Account", "ChkRef", "Debit", "Credit", "Date", "Description", "Tags")

        # Disabling the default column and setting the widths and headings for our columns
        self.transactions_viewer.column("#0", width=0, stretch=NO)
        self.transactions_viewer.column("Account", anchor=W, width=150)
        self.transactions_viewer.column("ChkRef", anchor=W, width=100)
        self.transactions_viewer.column("Debit", anchor=W, width=100)
        self.transactions_viewer.column("Credit", anchor=W, width=100)
        self.transactions_viewer.column("Date", anchor=W, width=100)
        self.transactions_viewer.column("Description", anchor=W, width=250)
        self.transactions_viewer.column("Tags", anchor=W, width=200)

        self.transactions_viewer.heading("#0", text="", anchor=W)
        self.transactions_viewer.heading("Account", text="Account", anchor=W)
        self.transactions_viewer.heading("ChkRef", text="ChkRef", anchor=W)
        self.transactions_viewer.heading("Debit", text="Debit", anchor=W)
        self.transactions_viewer.heading("Credit", text="Credit", anchor=W)
        self.transactions_viewer.heading("Date", text="Date", anchor=W)
        self.transactions_viewer.heading("Description", text="Description", anchor=W)
        self.transactions_viewer.heading("Tags", text="Tags", anchor=W)

        self.transactions_viewer.bind("<Double-1>", self.on_item_double_click)

    def on_item_double_click(self, event):
        row_id = self.transactions_viewer.identify_row(event.y)
        col_id = self.transactions_viewer.identify_column(event.x)
        # Only allow editing for the "Tags" column
        if col_id == "#7":  # Tags column
            x, y, width, height = self.transactions_viewer.bbox(row_id, col_id)
            current_value = self.transactions_viewer.item(row_id, "values")[6]
            self.editor = Entry(self.transactions_viewer)
            self.editor.place(x=x, y=y, width=width, height=height)
            self.editor.insert(0, current_value)
            self.editor.focus_set()
            self.editor.bind("<Return>", lambda e: self.update_tags(row_id))
            self.editor.bind("<FocusOut>", lambda e: self.update_tags(row_id))

    def update_tags(self, row_id):
        updated_value = self.editor.get()
        values = list(self.transactions_viewer.item(row_id, "values"))
        values[6] = updated_value
        self.transactions_viewer.item(row_id, values=values)
        self.editor.destroy()

    def preprocess_dataframe(self, filepath):
        df = pd.read_csv(filepath)
        df['Debit'] = df['Debit'].apply(lambda x: f"{x:.2f}" if pd.notnull(x) else "")
        df['Credit'] = df['Credit'].apply(lambda x: f"{x:.2f}" if pd.notnull(x) else "")
        object_columns = ['Account', 'ChkRef', 'Date', 'Description', 'Debit', 'Credit']
        df[object_columns] = df[object_columns].fillna("")
        return df

    def load_csv_to_table(self, filepath):
        for row in self.transactions_viewer.get_children():
            self.transactions_viewer.delete(row)
        df = self.preprocess_dataframe(filepath)
        for index, row in df.iterrows():
            self.transactions_viewer.insert(parent="", index="end", iid=index, values=row.tolist() + [""])

    def is_valid_csv_file(self, filepath):
        if filepath.endswith(".csv"):
            return True
        else:
            return False

    def view_transactions_from_file(self, filepath):
        if self.is_valid_csv_file(filepath):
            self.load_csv_to_table(filepath)
