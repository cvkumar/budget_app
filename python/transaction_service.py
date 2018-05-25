from flask import jsonify
# from transaction import Transaction
from datetime import datetime
from pony.orm import db_session
from database import Transaction


class TransactionService:
    def __init__(self):
        print("")

    def storeTransactions(self, transactionsResponse):
        with db_session:
            for transactionResponse in transactionsResponse:
                transactionEntity = Transaction(transaction_id=transactionResponse['transaction_id'],
                                                name=str(transactionResponse['name']),
                                                amount=transactionResponse['amount'],
                                                date=transactionResponse['date'],
                                                default_transaction_type=transactionResponse['transaction_type'],
                                                default_transaction_categories=transactionResponse['category'])

            print(transactionEntity)
