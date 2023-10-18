from tkinter import *
from tkinter.ttk import *

import pandas as pd


class TransactionViewer(Frame):
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
        self.transactions_viewer = Treeview(self.transactions_container)
        self.transactions_viewer.grid(row=0, column=1, sticky="nsew")
        self.configure_columns()
        self.configure_scrollbar()
        self.transactions_viewer.bind("<Double-1>", self.on_item_double_click)

    def configure_columns(self):
        column_config = {
            "Account": {"width": 150, "anchor": W, "heading": "Account"},
            "ChkRef": {"width": 100, "anchor": W, "heading": "ChkRef"},
            "Debit": {"width": 100, "anchor": W, "heading": "Debit"},
            "Credit": {"width": 100, "anchor": W, "heading": "Credit"},
            "Date": {"width": 100, "anchor": W, "heading": "Date"},
            "Description": {"width": 250, "anchor": W, "heading": "Description"},
            "Tags": {"width": 200, "anchor": W, "heading": "Tags"}
        }

        self.transactions_viewer["columns"] = tuple(column_config.keys())
        self.transactions_viewer.column("#0", width=0, stretch=NO)  # Disable default column

        for col, conf in column_config.items():
            self.transactions_viewer.column(col, width=conf["width"], anchor=conf["anchor"], stretch=conf.get("stretch", YES))
            self.transactions_viewer.heading(col, text=conf["heading"], anchor=conf["anchor"])

    def configure_scrollbar(self):
        self.scrollbar = Scrollbar(self.transactions_container, orient="vertical", command=self.transactions_viewer.yview)
        self.transactions_viewer.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=2, sticky="ns")

    def on_item_double_click(self, event):
        row_id = self.transactions_viewer.identify_row(event.y)
        col_id = self.transactions_viewer.identify_column(event.x)
        if not row_id or not col_id:
            return

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

    def display_transactions(self, filepath):
        if self.is_valid_csv_file(filepath):
            self.load_csv_to_table(filepath)
        else:
            print("Error: File must be a csv, xls, or xlsx file.")
