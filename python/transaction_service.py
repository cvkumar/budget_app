# from transaction import Transaction
from datetime import datetime
import pony.orm as pny
from database import Transaction


@pny.db_session
def retrieveTransactions():
    transactions = pny.select(transaction for transaction in Transaction)[:]
    return transactions


@pny.db_session
def storeTransactions(transactionsResponse):
    for transactionResponse in transactionsResponse:
        transactionEntity = Transaction(id=transactionResponse['transaction_id'],
                                        account_id=transactionResponse['account_id'],
                                        account_owner='Caleb Kumar',
                                        name=str(transactionResponse['name']),
                                        amount=transactionResponse['amount'],
                                        date=datetime.strptime(transactionResponse['date'], '%Y-%m-%d'),
                                        default_transaction_type=transactionResponse['transaction_type'],
                                        default_category1=str(transactionResponse['category']))
