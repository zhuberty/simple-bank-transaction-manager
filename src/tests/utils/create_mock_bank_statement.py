import csv
import os
from faker import Faker

fake = Faker()

def generate_bank_statement(num_entries=100):
    statement = []
    
    for _ in range(num_entries):
        account = fake.random_int(min=10000000, max=99999999)

        # 60% chance of missing check reference
        if fake.boolean(chance_of_getting_true=60):
            chk_ref = ''
        else:
            chk_ref = fake.random_int(min=1000, max=9999)

        debit = "{:.2f}".format(fake.random_int(min=1, max=500))
        credit = "{:.2f}".format(fake.random_int(min=1, max=500))
        date = fake.date_this_decade()
        description = fake.company()

        # Randomly choosing between debit and credit
        if fake.boolean():
            entry = (account, chk_ref, debit, '', date, description)
        else:
            entry = (account, chk_ref, '', credit, date, description)
        
        statement.append(entry)

    return statement

def write_to_csv(filename, data):
    if os.path.exists(filename):
        print(f"File '{filename}' already exists. No changes were made.")
        return

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Account", "ChkRef", "Debit", "Credit", "Date", "Description"])
        writer.writerows(data)
