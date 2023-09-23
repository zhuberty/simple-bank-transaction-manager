from ..categorizer import categorize
from ..transaction import Transaction
from ..report_generator import generate_report

def test_generate_report():
    transactions = [
        Transaction("", "", 100.00, "", "GROCERIES XYZ"),
        Transaction("", "", 50.00, "", "AMAZON SHOP"),
        Transaction("", "", -20.00, "", "GROCERIES XYZ"),
        Transaction("", "", 30.00, "", "AMAZON SHOP")
    ]

    # Categorize transactions
    for transaction in transactions:
        categorize(transaction)

    report = generate_report(transactions)
    
    assert report["Groceries"] == 80.00  # 100 - 20
    assert report["Online Shopping"] == 80.00  # 50 + 30
