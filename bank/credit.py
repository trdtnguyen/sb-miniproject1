"""
Credit class represents credits entity in our banking system
"""
__version__ = '0.1'
__author__ = 'Dat Nguyen'

from sqlalchemy.exc import DBAPIError
from sqlalchemy import Table, select, update, insert

from bank.credit_lineitem import CreditLineItem


class Credit:
    def __init__(self):
        self.id = 0
        self.cus_id = 0
        self.approved_by_emp_id = 0
        self.balance = 0.0
        self.apr = 0
        self.type = ''
        self.credit_score_required = 0
        self.cash_back = 0.0
        self.annual_fee = 0.0
        self.late_payment_fee = 0.0
        self.over_limit_fee = 0.0

    def load_data(self, db, id):
        """
        Load data into the instance by the input id
        :param db: Database instance
        :param id: customer id
        :return:
        """
        table = db.get_table('credits')
        conn = db.get_conn()
        logger = db.get_logger()
        try:
            s = select([table]).where(table.c.credit_id == id)
            results = conn.execute(s)
            if results.rowcount == 0:
                logger.info('Query return no results in Credit.load_data()')
                return 1
            elif results.rowcount > 1:
                logger.error('Query return too many results in Credit.load_data()')
                return 1
            else:
                row = results.first()
                self.id = row['credit_id']
                self.cus_id = row['cus_id']
                self.approved_by_emp_id = row['approved_by_employee_id']
                self.balance = row['credit_balance']
                self.apr = row['credit_apr']
                self.type = row['credit_type']
                self.credit_score_required = row['credit_credit_score_required']
                self.cash_back = row['credit_cash_back']
                self.annual_fee = row['credit_annual_fee']
                self.late_payment_fee = row['credit_late_payment_fee']
                self.over_limit_fee = row['credit_over_limit_fee']
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
        table = db.get_table('credits')
        conn = db.get_conn()
        logger = db.get_logger()
        try:
            s = select([table]).where(table.c.credit_id == self.id)
            results = conn.execute(s)
            if results.rowcount == 0:
                # Insert new row
                stmt = table.insert(). \
                    values(
                        cus_id=self.cus_id,
                        approved_by_employee_id=self.approved_by_emp_id,
                        credit_balance=self.balance,
                        credit_apr=self.apr,
                        credit_type=self.type,
                        credit_credit_score_required=self.credit_score_required,
                        credit_cash_back=self.cash_back,
                        credit_annual_fee=self.annual_fee,
                        credit_late_payment_fee=self.late_payment_fee,
                        credit_over_limit_fee=self.over_limit_fee
                    )
                conn.execute(stmt)
                return 0
            else:
                # Update
                stmt = table.update(). \
                    values(
                        cus_id=self.cus_id,
                        approved_by_employee_id=self.approved_by_emp_id,
                        credit_balance=self.balance,
                        credit_apr=self.apr,
                        credit_type=self.type,
                        credit_credit_score_required=self.credit_score_required,
                        credit_cash_back=self.cash_back,
                        credit_annual_fee=self.annual_fee,
                        credit_late_payment_fee=self.late_payment_fee,
                        credit_over_limit_fee=self.over_limit_fee
                    ). \
                    where(table.c.credit_id == self.id)
                conn.execute(stmt)
                return 0
        except DBAPIError:
            logger.error('Error Query')
            return 1

    def delete_data(self, db):
        table = db.get_table('credits')
        conn = db.get_conn()
        logger = db.get_logger()
        try:

            stmt = table.delete().\
                where(table.c.credit_id == self.id)
            conn.execute(stmt)
            return 0
        except DBAPIError:
            logger.error('Error Query')
            return 1

    def borrow_credit(self, db, processing_date, amount, description, pos):
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

        if amount <= 0:
            logger.error(f'Error invalid amount. Amount must be positive')
            return 1

        effective_date = processing_date

        acc_id = self.id
        cli = CreditLineItem(0, processing_date, effective_date, 'borrow', 'completed', amount, description, pos, acc_id)

        # Step 1: Insert the new transaction reflex the withdraw
        ret = cli.insert_lineitem(db)
        if ret != 0:
            # Error when inserting a new transaction
            return ret

        # Step 2: Update the corresponding row in accounts table

        conn = db.get_conn()
        credit_tb = db.get_table('credits')
        logger = db.get_logger()
        try:
            stmt = credit_tb.update(). \
                values(
                credit_balance=self.balance + amount,
            ). \
                where(credit_tb.c.credit_id == self.id)
            conn.execute(stmt)
            return 0
        except DBAPIError:
            logger.error('Error Query')
            return 1

    def pay_credit(self, db, processing_date, amount, description, pos):
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
        if amount > self.balance:
            logger.error(f'Could not pay more than balance. Amount: {amount}, balance {self.balance}')
            return 1
        if amount <= 0:
            logger.error(f'Error invalid amount. Amount must be positive')
            return 1

        effective_date = processing_date

        acc_id = self.id
        cli = CreditLineItem(0, processing_date, effective_date, 'pay', 'completed', amount, description, pos, acc_id)

        # Step 1: Insert the new transaction reflex the withdraw
        ret = cli.insert_lineitem(db)
        if ret != 0:
            # Error when inserting a new transaction
            return ret

        # Step 2: Update the corresponding row in accounts table

        conn = db.get_conn()
        credit_tb = db.get_table('credits')
        logger = db.get_logger()
        try:
            stmt = credit_tb.update(). \
                values(
                credit_balance=self.balance - amount,
            ). \
                where(credit_tb.c.credit_id == self.id)
            conn.execute(stmt)
            return 0
        except DBAPIError:
            logger.error('Error Query')
            return 1