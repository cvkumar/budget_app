class Transaction:
    def __init__(self, transaction_id, name, amount, date, default_transaction_type, default_categories):
        self.transaction_id = transaction_id
        self.name = name
        self.amount = amount
        self.date = date
        self.default_transaction_type = default_transaction_type
        self.default_categories = default_categories
        self.primary_category = None
        self.sub_category = None

    def __str__(self):
        return 'transaction id: {}, name: {}, amount: {}, date: {}, default_transaction_type: {}, default_categories: {}'.format(
            self.transaction_id, self.name, self.amount, self.date, self.default_transaction_type,
            self.default_categories)
