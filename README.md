# Spring Board miniproject1

This project simulates a Banking System with Python.

## Data Model
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

## How to use
