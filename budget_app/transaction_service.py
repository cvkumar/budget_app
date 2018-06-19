# from transaction import Transaction
from datetime import datetime
import pony.orm as pny
from database import Transaction
from uuid import uuid4


@pny.db_session
def retrieve_transactions():
    transactions = pny.select(transaction for transaction in Transaction)[:]
    return transactions


@pny.db_session
def store_transactions(transactionList):
    """

    :param transactionList: List of transactions where transactions are dictionary of item key to val
    :return: void
    """
    transactionEntities = []
    for transactionDict in transactionList:
        transactionEntity = Transaction(
            # Required Fields
            id=unicode(str(uuid4())),  # Generate this
            account_owner='Caleb Kumar',  # Hardcode
            name=str(transactionDict['name']),  # Required
            amount=transactionDict['amount'],  # Required
            date=datetime.strptime(transactionDict['date'], '%Y-%m-%d'),

            # Optional Fields
            transaction_type=str(transactionDict['transaction_type']),
            primary_category=str(transactionDict['primary_category']),
            secondary_category=str(transactionDict['secondary_category']))

        transactionEntities.append(transactionEntity)

    return transactionEntities


@pny.db_session
def store_plaid_transactions(transactionsResponse):
    for transactionResponse in transactionsResponse:
        transactionEntity = Transaction(id=transactionResponse['transaction_id'],
                                        account_id=transactionResponse['account_id'],
                                        account_owner='Caleb Kumar',
                                        name=str(transactionResponse['name']),
                                        amount=transactionResponse['amount'],
                                        date=datetime.strptime(transactionResponse['date'], '%Y-%m-%d'),
                                        default_transaction_type=transactionResponse['transaction_type'],
                                        # TODO: Iterate over list of categories
                                        default_category1=str(transactionResponse['category']))
