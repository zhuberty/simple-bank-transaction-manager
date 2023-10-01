import tkinter as tk
import pandas as pd
import os


class TransactionCategorizer(tk.Tk):
    def __init__(self, accounts_dir):
        super().__init__()

        self.accounts_dir = accounts_dir

        self.title("Transaction Categorizer")
        self.geometry("500x300")

        self.transactions = pd.DataFrame()
        self.load_transactions()

        self.transaction_listbox = tk.Listbox(self)
        self.transaction_listbox.pack(fill=tk.BOTH, expand=True)
        self.update_transaction_listbox()

        self.rule_name_label = tk.Label(self, text="Rule Name:")
        self.rule_name_label.pack()
        self.rule_name_entry = tk.Entry(self)
        self.rule_name_entry.pack()

        self.category_label = tk.Label(self, text="Category:")
        self.category_label.pack()
        self.category_entry = tk.Entry(self)
        self.category_entry.pack()

        self.apply_button = tk.Button(self, text="Apply Rule", command=self.apply_rule)
        self.apply_button.pack()

    def load_transactions(self):
        # Assume CSV files are in the same directory and have a 'description' column
        for file in os.listdir(self.accounts_dir):
            if file.endswith(".csv"):
                filepath = os.path.join(self.accounts_dir, file)
                df = pd.read_csv(filepath)
                self.transactions = pd.concat(
                    [self.transactions, df], ignore_index=True
                )

        # Explicitly create 'rule' and 'category' columns with data type 'object' (i.e., string)
        self.transactions["rule"] = ''
        self.transactions["category"] = ''

    def update_transaction_listbox(self):
        self.transaction_listbox.delete(0, tk.END)
        for transaction in self.transactions["Description"]:
            self.transaction_listbox.insert(tk.END, transaction)

    def apply_rule(self):
        selected_index = self.transaction_listbox.curselection()[0]
        selected_transaction = self.transactions.loc[selected_index, "Description"]
        rule_name = self.rule_name_entry.get()
        category = self.category_entry.get()
        mask = self.transactions["Description"].str.contains(selected_transaction)
        self.transactions.loc[mask, "category"] = category
        self.transactions.loc[mask, "rule"] = rule_name

        # Here you can save the updated DataFrame to a new CSV file or overwrite the existing ones
        self.transactions.to_csv('categorized_transactions.csv', index=False)

        self.update_transaction_listbox()
