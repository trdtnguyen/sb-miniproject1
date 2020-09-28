# Spring Board miniproject1

This project simulates a Banking System with Python.

## Setup
### Clone the repository
```
$ git clone https://github.com/trdtnguyen/sb-miniproject1.git
$ cd sb-miniproject1
```
### Set `PYTHONPATH`
Add location of the git clone directory to your `PYTHONPATH` environment variable.
* Linux / Mac:

Add the following line to your `~/.bashrc`
```
export PYTHONPATH=$PYTHONPATH;<path_to_git_clone>
```
* Windows
Open commnand promp using `Windows + R`. Open the window to edit user environment variable by following command:
```
rundll32.exe sysdm.cpl,EditEnvironmentVariables
```
Add location to the clone git directory to your `PYTHONPATH` **user** environment variable

### Install required Python packages
File `requirements.txt` contains necessary Python's packages for this project.
```
$ pip install -r requirements.txt
```
### Init Database
This project using MySQL 8.0 as the backend database.

MySQL installation guide for [Windows](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/windows-installation.html) and [Linux](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/linux-installation.html). 

* ***Create Database:*** Create a database named `bank`
```
$ mysqladmin -u root -p create bank
```
* ***Create tables:*** To create tables in `bank` database:
```
$ mysql -u root -p bank < sql/create_table.sql
``` 

* ***Insert sample data*** :
```
$ mysql -u root -p bank < sql/loaddata.sql
```
### Configuration
Open file `config.cnf` to customize your MySQL connection
```
[DATABASE]
host = localhost
user = root
pw = 12345678
db_name = bank
``` 
## Testing
This project use `pytest` to perform unit tests.
```
$ pytest test/test_db.py -v
```
## Data Model
[ERD diagram](docs/bank_ERD.pdf)
### Customers
* Customer is one of core entities in the banking system. 
* Each Customer entity represents for a customer in real life with full of personal information.
* Our system support internet banking for customers ***with the assumption that each user has only one login account*** for all of his/her banking accounts (e.g., checking, saving, loan).

### Employees
* Employee represents for a employee in real life with full of information in terms of HR's management.
* In this project, we keep Employee as simple as possible.

### Accounts
* `Accounts` represents an abstract bank account. One account could be saving, checking, certificates of deposit (CD), investment, and retirement accounts.
* One accound is created by an employee for a customer. So the `Accounts` should be link with `Customers` and `Employees` as described below.
* `Accounts` has a `+n:1` relationship with `Customers` with foreign key `cus_id`.
* `Accounts` has a `n:1` relationship with `Employees` with foreign key `created_by_emp_id`.
### Transactions
* `Transactions` represents tracsactions related with a bank account.
* `Transactions` has a `n:1` relationship with `Accounts`.
### Credits
* `Credits` represents the credit severice support by banking system.
* Similar to a bank account, credit account is approved by an employee for a customer. Thus, `Credits` has `n:1` relationships with `Customers` and `Employees`
* Different with a bank account, `Credits`has information of interest rate for late payment, cash back reward, and other fees such as over limit fee, cash advance fee.
### credit_line_items
* Similar to `Transactions` entity, `credit_line_items` works as a history log to keep track of transactions occured related with a credit account.
* `credit_line_items` has a `n:1` relationship with `Credits`.
### Loans
* 'Loans' represents the loan service support by banking system.
* Similar to `Credits`, `Loans` has interest rate and fees. However, `Loans` has a specific duration and various methods to pay the loan depend on loan types.
* `Loans` has a `n:1` relationships with `Customers` and `Employees`

### loan_line_items
* Similar to `credit_line_items` but for `Loans` entity.

## Class Design
[UML Diagram](docs/bank_uml.pdf)
* `bank` includes model classes that reflex corresponding entities from the [ERD diagram](docs/bank_ERD.pdf).
* There are three types of classes in this project
    * ***Independent class***: reflex independent entities such as `Customer`, `Employee`, `Account`, `Credit`, and `Loan`. Those classes could presents most of operations (such as load/update data from/to database) independently. 
    * ***Dependent class***: reflex line item entities such as: `Transaction`, `LineItem`, `CreditLineItem`, and `LoanLineItem`. Those classes are dependent on their corresponding classes and could not change the database by itself.
    * ***Utility class***: `DB` class is a utility class that support other classes access and query the database.

### Examples
Promote 