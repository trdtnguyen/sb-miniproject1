"""
Main
"""
__version__ = '0.1'
__author__ = 'Dat Nguyen'

from db.DB import DB
from bank.customer import Customer
import configparser


class Main:
    def __init__(self):
        self._connect_db()

    def _connect_db(self):
        config = configparser.ConfigParser()
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

cus = Customer()
cus.load_data(db, 10)
