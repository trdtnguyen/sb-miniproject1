"""
Main
"""
__version__ = '0.1'
__author__ = 'Dat Nguyen'

from bank.employee import Employee
from bank.account import Account
from bank.credit import Credit
from bank.loan import Loan
from db.DB import DB
from bank.customer import Customer
import configparser


class Main:
    def __init__(self):
        self._connect_db()

    def _connect_db(self):
        config = configparser.ConfigParser()
        #config.read('config.cnf')
        config.read('../config.cnf')
        # str_conn  = 'mysql+pymysql://root:12345678@localhost/bank'
        str_conn = 'mysql+pymysql://'
        str_conn += config['DATABASE']['user'] + ':' + config['DATABASE']['pw'] + \
                    '@' + config['DATABASE']['host'] + '/' + config['DATABASE']['db_name']
        print(str_conn)
        self.my_db = DB(str_conn)
        tb = self.my_db.get_table('customers')
        print(type(tb))
        print(tb.columns.keys())

    def get_db(self):
        return self.my_db


main = Main()
db = main.get_db()
#
# cus = Customer()
# cus.load_data(db, 1)
# cus.save_data(db)
#
# emp = Employee()
# emp.load_data(db, 1)
# emp.save_data(db)

emp = Employee()
emp.load_data(db, 1)
emp.promote(db, 2, 100005)

#
# acc = Account()
# acc.load_data(db, 1)
# acc.save_data(db)

# acc = Account()
# acc.load_data(db, 1)
# ret = acc.deposit(db, '2020-10-10', 100, "deposit check", "123 ATM Elm street")


# credit = Credit()
# credit.load_data(db, 1)
# credit.save_data(db)

# loan = Loan()
# loan.load_data(db, 1)
# loan.save_data(db)

# loan = Loan()
# loan.load_data(db, 1)
# loan.pay_loan(db, '2020-10-10', 100, "pay loan", "123 ATM Elm street")