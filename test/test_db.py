"""
Test Database
"""
__version__ = '0.1'
__author__ = 'Dat Nguyen'

from bank.loan import Loan
from db.DB import DB
from bank.customer import Customer
from bank.employee import Employee
from bank.account import Account
from bank.credit import Credit
import configparser
import pytest


@pytest.fixture
def db():
    config = configparser.ConfigParser()
    config.read('config.cnf')

    str_conn = 'mysql+pymysql://'
    str_conn += config['DATABASE']['user'] + ':' + config['DATABASE']['pw'] + \
                '@' + config['DATABASE']['host'] + '/' + config['DATABASE']['db_name']
    db = DB(str_conn)
    yield db
    db.close_connect()


def test_connect_db(db):
    """
    Test connection to the MySQL database
    :param db: Input db istance
    :return:
    """
    conn = db.get_conn()
    assert conn is not None


def test_load_existed_customer(db):
    cus = Customer()
    ret = cus.load_data(db, 1)
    assert ret == 0


def test_load_notexisted_customer(db):
    cus = Customer()
    ret = cus.load_data(db, 1000)
    assert ret != 0


def test_save_data_customer(db):
    cus = Customer()
    cus.load_data(db, 1)
    ret = cus.save_data(db)
    assert ret == 0


def test_load_existed_employee(db):
    emp = Employee()
    ret = emp.load_data(db, 1)
    assert ret == 0


def test_load_notexisted_employee(db):
    emp = Employee()
    ret = emp.load_data(db, 1000)
    assert ret != 0


def test_save_data_employee(db):
    emp = Employee()
    emp.load_data(db, 1)
    ret = emp.save_data(db)
    assert ret == 0


def test_promote_employee(db):
    emp = Employee()
    emp.load_data(db, 1)
    ret = emp.promote(db, 2, 100006)
    assert ret == 0


def test_load_existed_account(db):
    acc = Account()
    ret = acc.load_data(db, 1)
    assert ret == 0


def test_load_notexisted_account(db):
    acc = Account()
    ret = acc.load_data(db, 1000)
    assert ret != 0


def test_save_data_account(db):
    acc = Account()
    acc.load_data(db, 1)
    ret = acc.save_data(db)
    assert ret == 0


def test_withdraw_account(db):
    acc = Account()
    acc.load_data(db, 1)
    ret = acc.withdraw(db, '2020-10-10', 100, "pay electric bill", "123 internet")
    assert ret == 0


def test_deposit_account(db):
    acc = Account()
    acc.load_data(db, 1)
    ret = acc.deposit(db, '2020-10-10', 120, "deposit check", "123 ATM Elm street")
    assert ret == 0


def test_load_existed_credit(db):
    credit = Credit()
    ret = credit.load_data(db, 1)
    assert ret == 0

def test_load_notexisted_credit(db):
    credit = Credit()
    ret = credit.load_data(db, 1000)
    assert ret != 0

def test_load_pay(db):
    loan = Loan()
    loan.load_data(db, 1)
    loan.pay_loan(db, '2020-10-10', 100, "pay loan", "123 ATM Elm street")

def test_save_data_credit(db):
    credit = Credit()
    credit.load_data(db, 1)
    ret = credit.save_data(db)
    assert ret == 0


def test_load_existed_loan(db):
    loan = Loan()
    ret = loan.load_data(db, 1)
    assert ret == 0

def test_load_notexisted_loan(db):
    loan = Loan()
    ret = loan.load_data(db, 1000)
    assert ret != 0


def test_save_data_loan(db):
    loan = Loan()
    loan.load_data(db, 1)
    ret = loan.save_data(db)
    assert ret == 0