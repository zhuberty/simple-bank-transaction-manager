from ..transaction import Transaction

def test_transaction_initialization():
    transaction = Transaction("45253123", "7175", 491.00, "2022-06-18", "Wilson-Humphrey")
    assert transaction.account == "45253123"
    assert transaction.chkref == "7175"
    assert transaction.amount == 491.00
    assert transaction.date == "2022-06-18"
    assert transaction.description == "Wilson-Humphrey"
    assert transaction.category is None