class Transaction:
    def __init__(self, account, chkref, amount, date, description):
        self.account = account
        self.chkref = chkref
        self.date = date
        self.description = description
        self.category = None
        self.amount = float(amount)