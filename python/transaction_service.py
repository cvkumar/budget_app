from flask import jsonify
from transaction import Transaction
from datetime import datetime


class TransactionService:
    def __init__(self):
        print("")

    def parseTransactionResponse(self, response):
        transactionsResponse = response['transactions']

        for transactionResponse in transactionsResponse:
            # transaction = Transaction(transaction_id=transactionResponse['transaction_id'],
            #                           name=str(transactionResponse['name']),
            #                           amount=transactionResponse['amount'],
            #                           date=transactionResponse['date'],
            #                           default_transaction_type=transactionResponse['transaction_type'],
            #                           default_transaction_categories=transactionResponse['category'])

            print(transactionResponse['name'])
