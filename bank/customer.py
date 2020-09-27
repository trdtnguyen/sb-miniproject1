"""
Customer class represents customers entity in our banking system
"""
__version__ = '0.1'
__author__ = 'Dat Nguyen'

from sqlalchemy.exc import DBAPIError
from sqlalchemy import Table, select, update, insert


class Customer:
    def __init__(self):
        self.id = 0
        self.user_login_id = ''
        self.user_login_pw = ''
        self.fname = ''
        self.lname = ''
        self.address_street = ''
        self.address_city = ''
        self.address_state = ''
        self.address_zip = 0
        self.phone = ''
        self.email = ''
        self.dob = ''

    def load_data(self, db, id):
        """
        Load data into the instance by the input id
        :param db: Database instance
        :param id: customer id
        :return: 0 - data load successfully. 1 otherwise
        """
        customers = db.get_table('customers')
        conn = db.get_conn()
        logger = db.get_logger()
        try:
            s = select([customers]).where(customers.c.cus_id == id)
            results = conn.execute(s)
            if results.rowcount == 0:
                logger.info('Query return no results in Customer.load_data()')
                return 1
            elif results.rowcount > 1:
                logger.error('Query return too many results in Customer.load_data()')
                return 1
            else:
                row = results.first()
                self.id = row['cus_id']
                self.user_login_id = row['cus_user_login_id']
                self.user_login_pw = row['cus_user_login_pw']
                self.fname = row['cus_fname']
                self.lname = row['cus_lname']
                self.address_street = row['cus_address_street']
                self.address_city = row['cus_address_city']
                self.address_state = row['cus_address_state']
                self.address_zip = row['cus_address_zip']
                self.phone = row['cus_phone']
                self.email = row['cus_email']
                self.dob = row['cus_dob']
                return 0
        except DBAPIError:
            logger.error('Error Query')
            return 1

    def save_data(self, db):
        """
        save data from current instance into database
        If the current data is existed in the database, update it.
        Otherwise, insert it as a new row
        :return: 0 - save data successfully. 1 - Otherwise
        """
        customers = db.get_table('customers')
        conn = db.get_conn()
        logger = db.get_logger()
        try:
            s = select([customers]).where(customers.c.cus_id == self.id)
            results = conn.execute(s)
            if results.rowcount == 0:
                # Insert new row
                stmt = customers.insert(). \
                    values(cus_user_login_id=self.user_login_id,
                           cus_user_login_pw=self.user_login_pw,
                           cus_fname=self.fname,
                           cus_lname=self.lname,
                           cus_address_street=self.address_street,
                           cus_address_city=self.address_city,
                           cus_address_state=self.address_state,
                           cus_address_zip=self.address_zip,
                           cus_phone=self.phone,
                           cus_email=self.email,
                           cus_dob=self.dob)
                conn.execute(stmt)
                return 0
            else:
                # Update
                stmt = customers.update().\
                    values(cus_user_login_id = self.user_login_id,
                           cus_user_login_pw = self.user_login_pw,
                           cus_fname = self.fname,
                           cus_lname = self.lname,
                           cus_address_street = self.address_street,
                           cus_address_city = self.address_city,
                           cus_address_state = self.address_state,
                           cus_address_zip = self.address_zip,
                           cus_phone = self.phone,
                           cus_email = self.email,
                           cus_dob = self.dob).\
                    where(customers.c.cus_id == self.id)
                conn.execute(stmt)
                return 0
        except DBAPIError:
            logger.error('Error Query')
            return 1

    def delete_data(self, db):
        """
        Delete corresponding data with this instance in the database
        :param db: Input db instance
        :return: 0 if delete successfully. 1 otherwise
        """
        customers = db.get_table('customers')
        conn = db.get_conn()
        logger = db.get_logger()
        try:

            stmt = customers.delete().\
                where(customers.c.cus_id == self.id)
            conn.execute(stmt)
            return 0
        except DBAPIError:
            logger.error('Error Query')
            return 1