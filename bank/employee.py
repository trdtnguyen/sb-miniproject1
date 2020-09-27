"""
Employee class represents employees entity in our banking system
"""
__version__ = '0.1'
__author__ = 'Dat Nguyen'

from sqlalchemy.exc import DBAPIError
from sqlalchemy import Table, select, update, insert


class Employee:
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
        self.started_date = ''
        self.role = ''
        self.level = 0
        self.salary = 0.0

    def load_data(self, db, id):
        """
        Load data into the instance by the input id
        :param db: Database instance
        :param id: customer id
        :return:
        """
        table = db.get_table('employees')
        conn = db.get_conn()
        logger = db.get_logger()
        try:
            s = select([table]).where(table.c.emp_id == id)
            results = conn.execute(s)
            if results.rowcount == 0:
                logger.info('Query return no results in Employee.load_data()')
                return 1
            elif results.rowcount > 1:
                logger.error('Query return too many results in Employee.load_data()')
                return 1
            else:
                row = results.first()
                self.id = row['emp_id']
                self.user_login_id = row['emp_login_id']
                self.user_login_pw = row['emp_login_pw']
                self.fname = row['emp_fname']
                self.lname = row['emp_lname']
                self.address_street = row['emp_address_street']
                self.address_city = row['emp_address_city']
                self.address_state = row['emp_address_state']
                self.address_zip = row['emp_address_zip']
                self.phone = row['emp_phone']
                self.email = row['emp_email']
                self.dob = row['emp_dob']
                self.started_date = row['emp_started_date']
                self.role = row['emp_role']
                self.level = row['emp_level']
                self.salary = row['emp_salary']
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
        table = db.get_table('employees')
        conn = db.get_conn()
        logger = db.get_logger()
        try:
            s = select([table]).where(table.c.emp_id == self.id)
            results = conn.execute(s)
            if results.rowcount == 0:
                # Insert new row
                stmt = table.insert(). \
                    values( emp_login_id=self.user_login_id,
                            emp_login_pw=self.user_login_pw,
                            emp_fname=self.fname,
                            emp_lname=self.lname,
                            emp_address_street=self.address_street,
                            emp_address_city=self.address_city,
                            emp_address_state=self.address_state,
                            emp_address_zip=self.address_zip,
                            emp_phone=self.phone,
                            emp_email=self.email,
                            emp_dob=self.dob,
                            emp_started_date=self.started_date,
                            emp_role=self.role,
                            emp_level=self.level,
                            emp_salary=self.salary)
                conn.execute(stmt)
                return 0
            else:
                # Update
                stmt = table.update(). \
                    values(emp_login_id=self.user_login_id,
                           emp_login_pw=self.user_login_pw,
                           emp_fname=self.fname,
                           emp_lname=self.lname,
                           emp_address_street=self.address_street,
                           emp_address_city=self.address_city,
                           emp_address_state=self.address_state,
                           emp_address_zip=self.address_zip,
                           emp_phone=self.phone,
                           emp_email=self.email,
                           emp_dob=self.dob,
                           emp_started_date=self.started_date,
                           emp_role=self.role,
                           emp_level=self.level,
                           emp_salary=self.salary). \
                    where(table.c.emp_id == self.id)
                conn.execute(stmt)
                return 0
        except DBAPIError:
            logger.error('Error Query')
            return 1

    def delete_data(self, db):
        table = db.get_table('employees')
        conn = db.get_conn()
        logger = db.get_logger()
        try:

            stmt = table.delete().\
                where(table.c.emp_id == self.id)
            conn.execute(stmt)
            return 0
        except DBAPIError:
            logger.error('Error Query')
            return 1

    def promote(self, db, new_level, new_salary):
        """
        Promote current employee with new level and new salary.
        Update corresponding value in the current instance and the database.
        :param db:
        :param new_level:
        :param new_salary:
        :return: 0 if the action is success. 1 Otherwise
        """

        # We suppose that a promotion includes both increasing level and salary
        if self.level >= new_level or self.salary >= new_salary:
            return 1

        table = db.get_table('employees')
        conn = db.get_conn()
        logger = db.get_logger()
        try:
            stmt = table.update(). \
                values(
                       emp_level=new_level,
                       emp_salary=new_salary). \
                where(table.c.emp_id == self.id)
            conn.execute(stmt)
            self.level = new_level
            self.salary = new_salary
            return 0
        except DBAPIError:
            logger.error('Error Query')
            return 1