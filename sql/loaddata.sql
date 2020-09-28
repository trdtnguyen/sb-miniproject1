-- CUSTOMERS ------------------------------------------
INSERT INTO customers(
	cus_user_login_id, cus_user_login_pw, cus_fname, cus_lname, cus_address_street,
    cus_address_city, cus_address_state, cus_address_zip, cus_phone, cus_email, cus_dob)
VALUES ('Anna', '123456', 'Anna', 'An', '123 A St.', 'A city', 'AL', 12345, '0108201231', 'anna@gmail.com', '2000-10-10');

INSERT INTO customers(
	cus_user_login_id, cus_user_login_pw, cus_fname, cus_lname, cus_address_street,
    cus_address_city, cus_address_state, cus_address_zip, cus_phone, cus_email, cus_dob)
VALUES ('Ben', '123456', 'Ben', 'Bon', '331 B St.', 'B city', 'AK', 12315, '01082101231', 'ben@gmail.com', '1981-11-2');

INSERT INTO customers(
	cus_user_login_id, cus_user_login_pw, cus_fname, cus_lname, cus_address_street,
    cus_address_city, cus_address_state, cus_address_zip, cus_phone, cus_email, cus_dob)
VALUES ('Christ', '123456', 'Christ', 'Matt', '3112 C St.', 'C city', 'CA', 78315, '01080901231', 'christ@gmail.com', '1985-12-11');

INSERT INTO customers(
	cus_user_login_id, cus_user_login_pw, cus_fname, cus_lname, cus_address_street,
    cus_address_city, cus_address_state, cus_address_zip, cus_phone, cus_email, cus_dob)
VALUES ('Dan', '123456', 'Dan', 'Ng', '12 D St.', 'D city', 'DE', 38315, '01081901231', 'dan@gmail.com', '1985-05-12');

-- EMPLOYEES ------------------------------------------
INSERT INTO employees(
    emp_login_id, emp_login_pw, emp_fname, emp_lname, 
    emp_address_street, emp_address_city, emp_address_state, emp_address_zip,
    emp_phone, emp_email, emp_dob, emp_started_date, emp_role, emp_level, emp_salary)
VALUES ('Anny', '123456', 'Anny', 'Whitney', '456 A St.', 'A city', 'AL', 12345, '0103231872', 'anny@gmail.com', '2002-1-12', '2010-10-1', 'Officer', 1, 65000);

INSERT INTO employees(
    emp_login_id, emp_login_pw, emp_fname, emp_lname, 
    emp_address_street, emp_address_city, emp_address_state, emp_address_zip,
    emp_phone, emp_email, emp_dob, emp_started_date, emp_role, emp_level, emp_salary)
VALUES ('Bob', '123456', 'Bob', 'Krush', '456 B St.', 'B city', 'AK', 12215, '0103121872', 'bob@gmail.com', '1988-11-2', '2000-1-20', 'Manager', 3, 85000);

INSERT INTO employees(
    emp_login_id, emp_login_pw, emp_fname, emp_lname, 
    emp_address_street, emp_address_city, emp_address_state, emp_address_zip,
    emp_phone, emp_email, emp_dob, emp_started_date, emp_role, emp_level, emp_salary)
VALUES ('Cessi', '123456', 'Cessi', 'Black', '212 C St.', 'C city', 'CA', 42115, '0103151872', 'cessi@gmail.com', '2001-10-2', '2019-10-2', 'Officer', 1, 55000);

-- ACCOUNTS ------------------------------------------
INSERT INTO accounts(
    cus_id, acc_type, acc_status, acc_balance, acc_open_date, 
    acc_apr, acc_withdrawal_limits, acc_annual_fee, acc_min_balance_required, created_by_emp_id)
VALUES(1, 'Checking', 'Active', '3200','2000-12-2', 0.001, 0, 0, 0, 1);

INSERT INTO accounts(
    cus_id, acc_type, acc_status, acc_balance, acc_open_date, 
    acc_apr, acc_withdrawal_limits, acc_annual_fee, acc_min_balance_required, created_by_emp_id)
VALUES(1, 'Saving', 'Active', '20000','2000-12-2', 0.002, 0, 0, 200, 1);

INSERT INTO accounts(
    cus_id, acc_type, acc_status, acc_balance, acc_open_date, 
    acc_apr, acc_withdrawal_limits, acc_annual_fee, acc_min_balance_required, created_by_emp_id)
VALUES(1, 'CD', 'Active', '12000','2000-12-2', 0.003, 0, 0, 500, 1);

INSERT INTO accounts(
    cus_id, acc_type, acc_status, acc_balance, acc_open_date, 
    acc_apr, acc_withdrawal_limits, acc_annual_fee, acc_min_balance_required, created_by_emp_id)
VALUES(2, 'Checking', 'Active', '200','2010-10-11', 0.001, 0, 0, 0, 1);
INSERT INTO accounts(
    cus_id, acc_type, acc_status, acc_balance, acc_open_date, 
    acc_apr, acc_withdrawal_limits, acc_annual_fee, acc_min_balance_required, created_by_emp_id)
VALUES(2, 'Saving', 'Active', '1000','2010-10-11', 0.002, 0, 0, 200, 1);

INSERT INTO accounts(
    cus_id, acc_type, acc_status, acc_balance, acc_open_date, 
    acc_apr, acc_withdrawal_limits, acc_annual_fee, acc_min_balance_required, created_by_emp_id)
VALUES(3, 'Saving', 'Active', '1200','2010-10-11', 0.002, 0, 0, 200, 2);

INSERT INTO accounts(
    cus_id, acc_type, acc_status, acc_balance, acc_open_date, 
    acc_apr, acc_withdrawal_limits, acc_annual_fee, acc_min_balance_required, created_by_emp_id)
VALUES(3, 'CD', 'Active', '22000','2011-3-2', 0.003, 0, 0, 500, 2);

-- LOANS ------------------------------------------

INSERT INTO loans(
    cus_id, approved_by_employee_id, loan_original_amount, loan_remain_amount,
    loan_apr, loan_duration, loan_type, loan_credit_score_required, loan_consequence_for_not_paying)
VALUES(1, 3, 20000, 18000, 0.05, 5, 'Student Loan', 450, 'N/A');
INSERT INTO loans(
    cus_id, approved_by_employee_id, loan_original_amount, loan_remain_amount,
    loan_apr, loan_duration, loan_type, loan_credit_score_required, loan_consequence_for_not_paying)
VALUES(2, 3, 32000, 30000, 0.07, 5, 'Car Title Loan', 550, 'Car Repossessed');

INSERT INTO loans(
    cus_id, approved_by_employee_id, loan_original_amount, loan_remain_amount,
    loan_apr, loan_duration, loan_type, loan_credit_score_required, loan_consequence_for_not_paying)
VALUES(3, 3, 310000, 200000, 0.04, 15, 'Mortgage Loan', 600, 'House Repossessed');

-- CREDITS ------------------------------------------
INSERT INTO credits(
    cus_id, approved_by_employee_id, credit_balance, credit_apr, credit_type,
    credit_credit_score_required, credit_cash_back, credit_annual_fee, 
    credit_late_payment_fee, credit_over_limit_fee)
VALUES(1, 1, 0, 0.1, 'Secured', 320, 0, 120, 0, 20);

INSERT INTO credits(
    cus_id, approved_by_employee_id, credit_balance, credit_apr, credit_type,
    credit_credit_score_required, credit_cash_back, credit_annual_fee, 
    credit_late_payment_fee, credit_over_limit_fee)
VALUES(2, 1, 2000, 0.15, 'Normal', 320, 0, 120, 200, 20);

INSERT INTO credits(
    cus_id, approved_by_employee_id, credit_balance, credit_apr, credit_type,
    credit_credit_score_required, credit_cash_back, credit_annual_fee, 
    credit_late_payment_fee, credit_over_limit_fee)
VALUES(3, 2, 0, 0.15, 'Normal', 320, 200, 120, 0, 20);