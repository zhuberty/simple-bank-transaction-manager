def categorize(transaction):
    # Simple categorization logic for the prototype
    if "GROCERIES" in transaction.description.upper():
        transaction.category = "Groceries"
    elif "AMAZON" in transaction.description.upper():
        transaction.category = "Online Shopping"
    else:
        transaction.category = "Unknown"
