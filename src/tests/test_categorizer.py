from src.categorizer import categorize
from src.transaction import Transaction

def test_categorizer():
    grocery_transaction = Transaction("", "", 100.00, "", "GROCERIES XYZ")
    amazon_transaction = Transaction("", "", 50.00, "", "AMAZON SHOP")
    unknown_transaction = Transaction("", "", 25.00, "", "UNKNOWN SHOP")
    
    categorize(grocery_transaction)
    categorize(amazon_transaction)
    categorize(unknown_transaction)
    
    assert grocery_transaction.category == "Groceries"
    assert amazon_transaction.category == "Online Shopping"
    assert unknown_transaction.category == "Unknown"
