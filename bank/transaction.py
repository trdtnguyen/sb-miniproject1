"""
Transaction class represents transaction entity in our banking system
"""
__version__ = '0.1'
__author__ = 'Dat Nguyen'

from sqlalchemy.exc import DBAPIError

from bank.lineitem import LineItem
from sqlalchemy import insert, select, create_engine, MetaData, Table


class Transaction(LineItem):

    def __init__(self, in_id, in_processing_date, in_effective_date,
                 in_type, in_status, in_amount, in_description, in_pos, in_acc_id):
        """ Constructor
        Args:
            self (obj): self obj
            in_processing_date (str): processing date from database
            in_type (str): type of transaction. It is either "deposit" or "withdraw".
            in_status (str): status of the transaction. It is either "Pending" or "Completed".
            in_amount (float): amount value of transaction
            in_description (str): description of the transaction
            in_pos (str): location of the pos that the transaction is occured
            in_acc_id (int): bank account id
        Returns:
            None
        """
        LineItem.__init__(self, in_id, in_processing_date, in_effective_date,
                          in_type, in_status, in_amount, in_description, in_pos)
        self.acc_id = in_acc_id

    def insert_transaction(self, db):
        """ Insert a new row to corresponding table in database. The row are fetched from current instance properties.
        Args:
            db (DB): DB instance
        Returns:
            None
        """
        table = db.get_table('transactions')
        conn = db.get_conn()
        logger = db.get_logger()
        try:
            stmt = table.insert(). \
                values(
                    trans_processing_date=self.processing_date,
                    trans_effective_date=self.effective_date,
                    trans_type=self.type,
                    trans_status=self.status,
                    acc_id=self.acc_id,
                    trans_amount=self.amount,
                    trans_description=self.description,
                    trans_pos=self.pos
                )
            conn.execute(stmt)
            return 0
        except DBAPIError:
            logger.error('Error Query')
            return 1
