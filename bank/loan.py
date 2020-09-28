"""
Loan class represents loans entity in our banking system
"""
__version__ = '0.1'
__author__ = 'Dat Nguyen'

from sqlalchemy.exc import DBAPIError
from sqlalchemy import Table, select, update, insert

from bank.loan_lineitem import LoanLineItem


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
            s = select([table]).where(table.c.loan_id == id)
            results = conn.execute(s)
            if results.rowcount == 0:
                logger.info('Query return no results in Loan.load_data()')
                return 1
            elif results.rowcount > 1:
                logger.error('Query return too many results in Loan.load_data()')
                return 1
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
                return 0

        except DBAPIError:
            logger.error('Error Query')
            return 1

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
            s = select([table]).where(table.c.loan_id == self.id)
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
                return 0
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
                    ). \
                    where(table.c.loan_id == self.id)
                conn.execute(stmt)
                return 0
        except DBAPIError:
            logger.error('Error Query')
            return 1

    def delete_data(self, db):
        table = db.get_table('loans')
        conn = db.get_conn()
        logger = db.get_logger()
        try:

            stmt = table.delete().\
                where(table.c.loan_id == self.id)
            conn.execute(stmt)
            return 0
        except DBAPIError:
            logger.error('Error Query')
            return 1

    def pay_loan(self, db, processing_date, amount, description, pos):
        """
        Pay a loan monthly
        :param db:
        :param processing_date:
        :param amount:
        :param description:
        :param pos:
        :return:
        """
        logger = db.get_logger()

        # Logical checking
        if self.remain_amount < amount:
            logger.error(f'Error, could not pay an amount more than remain. Remain amount: {self.remain_amount}, pay {amount}')
            return 1

        if amount <= 0:
            logger.error(f'Error invalid amount. Amount must be positive')
            return 1

        effective_date = processing_date

        acc_id = self.id
        lli = LoanLineItem(0, processing_date, effective_date, 'loanpay', 'pending', amount, description, pos, acc_id)

        # Step 1: Insert the new transaction reflex the withdraw
        ret = lli.insert_lineitem(db)
        if ret != 0:
            # Error when inserting a new transaction
            return ret

        # Step 2: Update the corresponding row in accounts table

        conn = db.get_conn()
        loan_tb = db.get_table('loans')
        logger = db.get_logger()
        try:
            stmt = loan_tb.update(). \
                values(
                loan_remain_amount=self.remain_amount - amount,
            ). \
                where(loan_tb.c.loan_id == self.id)
            conn.execute(stmt)
            return 0
        except DBAPIError:
            logger.error('Error Query')
            return 1