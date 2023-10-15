from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog

import pandas as pd


class ClientFrameMain(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure_grid()
        self.configure_admin_btn()
        self.configure_import_file_btn()
        self.configure_preview_file_btn()
        self.configure_transactions_viewer()

    def configure_grid(self):
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.btn_container = Frame(self)
        self.btn_container.grid(row=0, column=0, sticky="nsew")
        self.btn_container.grid_columnconfigure(0, weight=1)
        self.btn_container.grid_columnconfigure(1, weight=1)
        self.btn_container.grid_columnconfigure(2, weight=1)
        self.transactions_container = Frame(self)
        self.transactions_container.grid(row=1, column=0, sticky="nsew")
        self.transactions_container.grid_columnconfigure(0, weight=0)
        self.transactions_container.grid_columnconfigure(1, weight=1)
        self.transactions_container.grid_columnconfigure(2, weight=0)

    def configure_admin_btn(self):
        self.admin_btn = Button(
            self.btn_container,
            text="Go to Admin",
            command=lambda: self.controller.show_frame("admin"),
        )
        self.admin_btn.grid(row=0, column=0, sticky="ew")

    def configure_import_file_btn(self):
        self.import_file_btn = Button(
            self.btn_container,
            text="Import File",
            command=self.import_file_btn_event,
        )
        self.import_file_btn.grid(row=0, column=1, sticky="ew")
    
    def configure_preview_file_btn(self):
        self.preview_file_btn = Button(
            self.btn_container,
            text="Preview File",
            command=self.preview_file_btn_event,
        )
        self.preview_file_btn.grid(row=0, column=2, sticky="ew")

    def preview_file_btn_event(self):
        # select file dialog
        dialog_result = filedialog.askopenfilename(
            title="Select CSV File to Preview",
            filetypes=(("csv files", ".csv"), ("all files", "*.*"))
        )
        self.view_transactions_from_file(dialog_result)

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
            # Get the bounding box of the cell to place the Entry widget
            x, y, width, height = self.transactions_viewer.bbox(row_id, col_id)

            # Fetch the current value of the cell
            current_value = self.transactions_viewer.item(row_id, "values")[6]

            # Create and place the Entry widget
            self.editor = Entry(self.transactions_viewer)
            self.editor.place(x=x, y=y, width=width, height=height)
            self.editor.insert(0, current_value)
            self.editor.focus_set()
            self.editor.bind("<Return>", lambda e: self.update_tags(row_id))
            self.editor.bind("<FocusOut>", lambda e: self.update_tags(row_id))

    def update_tags(self, row_id):
        # Get the updated value from the Entry widget
        updated_value = self.editor.get()

        # Update the treeview item's value
        values = list(self.transactions_viewer.item(row_id, "values"))
        values[6] = updated_value
        self.transactions_viewer.item(row_id, values=values)

        # Remove the Entry widget
        self.editor.destroy()

    def preprocess_dataframe(self, filepath):
        df = pd.read_csv(filepath)
        
        # Convert 'Debit' and 'Credit' to two decimal places
        df['Debit'] = df['Debit'].apply(lambda x: f"{x:.2f}" if pd.notnull(x) else "")
        df['Credit'] = df['Credit'].apply(lambda x: f"{x:.2f}" if pd.notnull(x) else "")

        # Replace NaN values with blank only for columns that should be of type 'object'
        object_columns = ['Account', 'ChkRef', 'Date', 'Description', 'Debit', 'Credit']  # Add/remove based on your specific columns
        df[object_columns] = df[object_columns].fillna("")

        return df


    def load_csv_to_table(self, filepath):
        # Clear existing rows in the table
        for row in self.transactions_viewer.get_children():
            self.transactions_viewer.delete(row)

        # Preprocess the data
        df = self.preprocess_dataframe(filepath)

        # Insert data into the table
        for index, row in df.iterrows():
            self.transactions_viewer.insert(parent="", index="end", iid=index, values=row.tolist() + [""])


    def import_file_btn_event(self):
        import_file_window = Toplevel(self)
        import_file_window.title("Import File")

        select_file_btn = Button(
            import_file_window,
            text="Select File",
            command=lambda: self.open_file_dialog(import_file_window)
        )

    def open_file_dialog(self, import_file_window):
        dialog_result = filedialog.askopenfilename(
            title="Select CSV File to Import",
            filetypes=(("csv files", ".csv"), ("all files", "*.*"))
        )
        self.open_file_dialog_callback(dialog_result, import_file_window)

    def open_file_dialog_callback(self, dialog_result, import_file_window):
        if dialog_result.endswith(".csv"):
            self.controller.frames["admin"].log_message("Importing file: " + dialog_result)
        else:
            self.controller.frames["admin"].log_message("Error: File must be a csv file")
        import_file_window.destroy()

    def is_valid_csv_file(self, filepath):
        if filepath.endswith(".csv"):
            return True
        else:
            return False

    def view_transactions_from_file(self, filepath):
        if self.is_valid_csv_file(filepath):
            self.load_csv_to_table(filepath)
        else:
            self.controller.frames["admin"].log_message("Error: File must be a csv file")
