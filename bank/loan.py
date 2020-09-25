"""
Loan class represents loans entity in our banking system
"""
__version__ = '0.1'
__author__ = 'Dat Nguyen'

from sqlalchemy.exc import DBAPIError
from sqlalchemy import Table, select, update, insert


class Loan:
    def __init__(self):
        self.id = 0
        self.cus_id = 0
        self.approved_by_emp_id = 0
        self.original_amount = 0.0
        self.remain_amount = 0.0
        self.apr = 0
        self.duration = 0
        self.type = ''
        self.credit_score_required = 0
        self.consequence_for_not_paying = ''

    def load_data(self, db, id):
        """
        Load data into the instance by the input id
        :param db: Database instance
        :param id: customer id
        :return:
        """
        table = db.get_table('loans')
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
                self.id = row['loan_id']
                self.cus_id = row['cus_id']
                self.approved_by_emp_id = row['approved_by_employee_id']
                self.original_amount = row['loan_original_amount']
                self.remain_amount = row['loan_remain_amount']
                self.apr = row['loan_apr']
                self.duration = row['loan_duration']
                self.type = row['loan_type']
                self.credit_score_required = row['loan_credit_score_required']
                self.consequence_for_not_paying = row['loan_consequence_for_not_paying']

        except DBAPIError:
            logger.error('Error Query')

    def save_data(self, db):
        """
        save data from current instance into database
        If the current data is existed in the database, update it.
        Otherwise, insert it as a new row
        :return: None
        """
        table = db.get_table('loans')
        conn = db.get_conn()
        logger = db.get_logger()
        try:
            s = select([table]).where(table.c.loan_id == id)
            results = conn.execute(s)
            if results.rowcount == 0:
                # Insert new row
                stmt = table.insert(). \
                    values(
                        cus_id=self.cus_id,
                        approved_by_employee_id=self.approved_by_emp_id,
                        loan_original_amount=self.original_amount,
                        loan_remain_amount=self.remain_amount,
                        loan_apr=self.apr,
                        loan_duration=self.duration,
                        loan_type=self.type,
                        loan_credit_score_required=self.credit_score_required,
                        loan_consequence_for_not_paying=self.consequence_for_not_paying
                    )
                conn.execute(stmt)
            else:
                # Update
                stmt = table.update(). \
                    values(
                        cus_id=self.cus_id,
                        approved_by_employee_id=self.approved_by_emp_id,
                        loan_original_amount=self.original_amount,
                        loan_remain_amount=self.remain_amount,
                        loan_apr=self.apr,
                        loan_duration=self.duration,
                        loan_type=self.type,
                        loan_credit_score_required=self.credit_score_required,
                        loan_consequence_for_not_paying=self.consequence_for_not_paying
                    )
                conn.execute(stmt)
        except DBAPIError:
            logger.error('Error Query')

    def delete_data(self, db):
        table = db.get_table('loans')
        conn = db.get_conn()
        logger = db.get_logger()
        try:

            stmt = table.delete().\
                where(table.c.loan_id == self.id)
            conn.execute(stmt)
        except DBAPIError:
            logger.error('Error Query')