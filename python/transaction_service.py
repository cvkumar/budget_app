from flask import jsonify
# from transaction import Transaction
from datetime import datetime
from pony.orm import db_session
import pony.orm as pny
from database import Transaction


@pny.db_session
class TransactionService:
    def __init__(self):
        print("")

    @pny.db_session
    def storeTransactions(self, transactionsResponse):
        for transactionResponse in transactionsResponse:
            print transactionResponse

            transactionEntity = Transaction(id=transactionResponse['transaction_id'],
                                            account_id=transactionResponse['account_id'],
                                            # account_owner='Caleb Kumar',
                                            name=str(transactionResponse['name']),
                                            amount=transactionResponse['amount'],
                                            date=datetime.strptime(transactionResponse['date'], '%Y-%m-%d'),
                                            default_transaction_type=transactionResponse['transaction_type'],
                                            default_category1=str(transactionResponse['category']))

            print(transactionEntity)
