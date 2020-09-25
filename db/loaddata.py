"""
Load sample data to the database
"""
__version__ = '0.1'
__author__ = 'Dat Nguyen'

import pymysql
from sqlalchemy import insert, select, create_engine, MetaData, Table

def create_tables():

    engine = create_engine('mysql+pymysql://root:12345678@localhost/bank',pool_recycle=3600)
    connection = engine.connect()

    metadata = MetaData()

    customers_tb = Table('customers', metadata, autoload=True, autoload_with=engine)
    employees_tb = Table('employees', metadata, autoload=True, autoload_with=engine)
    accounts_tb = Table('accounts', metadata, autoload=True, autoload_with=engine)
    transactions_tb = Table('transactions', metadata, autoload=True, autoload_with=engine)
    loans_tb = Table('loans', metadata, autoload=True, autoload_with=engine)
    lli_tb = Table('loan_line_items', metadata, autoload=True, autoload_with=engine)
    credits_tb = Table('credits', metadata, autoload=True, autoload_with=engine)
    cli_tb = Table('credit_line_items', metadata, autoload=True, autoload_with=engine)

    print(accounts_tb.columns.keys())
    connection.close()
# customers_val_list = [
#     {'cus_user_login_id' : 'anna',
#      'cus_user_login_pw' : '123abc',
#      'cus_fname' : 'Anna',
#      'cus_lname' : 'Young',
#      'cus_address_street' : '123 Oak Dr',
#      'cus_address_city' : 'Peace',
#      'cus_address_state' : 'CA',
#      'cus_address_zip' : '275341',
#      'cus_phone' : '0107288791',
#      'cus_email' : 'annayoung@gmail.com',
#      'cus_dob':'2000-10-12'
#      }
# ]
#
# stmt = insert(customers_tb)
# results = connection.execute(stmt, customers_val_list)
# print(results.rowcount)

