"""
Account class represents account entity in our banking system
"""
__version__ = '0.1'
__author__ = 'Dat Nguyen'

from sqlalchemy.exc import DBAPIError
from sqlalchemy import Table, select, update, insert


class Account:
    def __init__(self):
        self.id = 0
        self.cus_id = 0
        self.type = ''
        self.status = ''
        self.balance = 0.0
        self.open_date = ''
        self.apr = 0.0
        self.withdrawal_limits = 0.0
        self.annual_fee = 0.0
        self.min_balance_required = 0.0
        self.created_by_emp_id = 0

    def load_data(self, db, id):
        """
        Load data into the instance by the input id
        :param db: Database instance
        :param id: customer id
        :return:
        """
        table = db.get_table('accounts')
        conn = db.get_conn()
        logger = db.get_logger()
        try:
            s = select([table]).where(table.c.acc_id == id)
            results = conn.execute(s)
            if results.rowcount == 0:
                logger.info('Query return no results in Account.load_data()')
            elif results.rowcount > 1:
                logger.error('Query return too many results in Account.load_data()')
            else:
                row = results.first()
                self.id = row['acc_id']
                self.cus_id = row['cus_id']
                self.type = row['acc_type']
                self.status = row['acc_status']
                self.balance = row['acc_balance']
                self.open_date = row['acc_open_date']
                self.apr = row['acc_apr']
                self.withdrawal_limits = row['acc_withdrawal_limits']
                self.annual_fee = row['acc_annual_fee']
                self.min_balance_required = row['acc_min_balance_required']
                self.created_by_emp_id = row['created_by_emp_id']

        except DBAPIError:
            logger.error('Error Query')

    def save_data(self, db):
        """
        save data from current instance into database
        If the current data is existed in the database, update it.
        Otherwise, insert it as a new row
        :return: None
        """
        table = db.get_table('accounts')
        conn = db.get_conn()
        logger = db.get_logger()
        try:
            s = select([table]).where(table.c.acc_id == id)
            results = conn.execute(s)
            if results.rowcount == 0:
                # Insert new row
                stmt = table.insert(). \
                    values(
                        cus_id=self.cus_id,
                        acc_type=self.type,
                        acc_status=self.status,
                        acc_balance=self.balance,
                        acc_open_date=self.open_date,
                        acc_apr=self.apr,
                        acc_withdrawal_limits=self.withdrawal_limits,
                        acc_annual_fee=self.annual_fee,
                        acc_min_balance_required=self.min_balance_required,
                        created_by_emp_id=self.created_by_emp_id
                    )
                conn.execute(stmt)
            else:
                # Update
                stmt = table.update(). \
                    values(
                        cus_id=self.cus_id,
                        acc_type=self.type,
                        acc_status=self.status,
                        acc_balance=self.balance,
                        acc_open_date=self.open_date,
                        acc_apr=self.apr,
                        acc_withdrawal_limits=self.withdrawal_limits,
                        acc_annual_fee=self.annual_fee,
                        acc_min_balance_required=self.min_balance_required,
                        created_by_emp_id=self.created_by_emp_id
                    )
                conn.execute(stmt)
        except DBAPIError:
            logger.error('Error Query')

    def delete_data(self, db):
        table = db.get_table('accounts')
        conn = db.get_conn()
        logger = db.get_logger()
        try:

            stmt = table.delete().\
                where(table.c.acc_id == self.id)
            conn.execute(stmt)
        except DBAPIError:
            logger.error('Error Query')