def generate_report(transactions):
    category_totals = {}
    for transaction in transactions:
        category_totals[transaction.category] = category_totals.get(transaction.category, 0) + transaction.amount
    return category_totals
