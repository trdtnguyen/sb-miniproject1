DROP TABLE IF EXISTS credit_line_items;
DROP TABLE IF EXISTS credits;
DROP TABLE IF EXISTS loan_line_items;
DROP TABLE IF EXISTS loans;
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS employees;

CREATE TABLE IF NOT EXISTS customers(
	cus_id BIGINT NOT NULL auto_increment,
    cus_user_login_id VARCHAR(64),
    cus_user_login_pw VARCHAR(64),
    cus_fname VARCHAR(32) NOT NULL,
    cus_lname VARCHAR(32) NOT NULL,
    cus_address_street VARCHAR(64) NOT NULL,
    cus_address_city VARCHAR(32) NOT NULL,
    cus_address_state VARCHAR(2) NOT NULL,
    cus_address_zip INT NOT NULL,
    cus_phone VARCHAR(45) NULL,
    cus_email VARCHAR(45) NULL,
    cus_dob DATETIME,
    
    PRIMARY KEY(cus_id)
);
CREATE TABLE IF NOT EXISTS employees(
	emp_id BIGINT NOT NULL auto_increment,
    emp_login_id VARCHAR(64),
    emp_login_pw VARCHAR(64),
    emp_fname VARCHAR(32) NOT NULL,
    emp_lname VARCHAR(32) NOT NULL,
    emp_address_street VARCHAR(64) NOT NULL,
    emp_address_city VARCHAR(32) NOT NULL,
    emp_address_state VARCHAR(2) NOT NULL,
    emp_address_zip INT NOT NULL,
    emp_phone VARCHAR(45) NULL,
    emp_email VARCHAR(45) NULL,
    emp_dob DATETIME,
    emp_started_date DATETIME,
    emp_role VARCHAR(128),
    emp_level INT,
    emp_salary FLOAT,
    

	PRIMARY KEY (emp_id)
);
CREATE TABLE IF NOT EXISTS accounts(
	acc_id BIGINT NOT NULL auto_increment,
    cus_id BIGINT NOT NULL,
    acc_type VARCHAR(32),
    acc_status VARCHAR(32),
    acc_balance FLOAT,
    acc_open_date TIMESTAMP,
    acc_apr FLOAT,
    acc_withdrawal_limits FLOAT,
    acc_annual_fee FLOAT,
    acc_min_balance_required FLOAT,
    created_by_emp_id BIGINT,
    PRIMARY KEY (acc_id),
    FOREIGN KEY (cus_id) REFERENCES customers(cus_id),
    FOREIGN KEY (created_by_emp_id) REFERENCES employees(emp_id)
);

CREATE TABLE IF NOT EXISTS transactions(
	trans_id BIGINT NOT NULL auto_increment,
    trans_processing_date DATETIME NOT NULL,
    trans_effective_date DATETIME NOT NULL,
    trans_type VARCHAR(32),
    trans_status VARCHAR(32),
    acc_id BIGINT NOT NULL,
    trans_amount FLOAT,
    trans_description TEXT,
    trans_pos TEXT,
    
    PRIMARY KEY (trans_id),
    FOREIGN KEY (acc_id) REFERENCES accounts(acc_id)
);
CREATE TABLE IF NOT EXISTS loans(
	loan_id BIGINT NOT NULL auto_increment,
    cus_id BIGINT NOT NULL,
    approved_by_employee_id BIGINT NOT NULL,
    loan_original_amount FLOAT,
    loan_remain_amount FLOAT,
    loan_apr FLOAT,
    loan_duration INT,
    loan_type VARCHAR(32),
    loan_credit_score_required INT,
    loan_consequence_for_not_paying VARCHAR(64),
    
    PRIMARY KEY (loan_id),
    FOREIGN KEY (cus_id) REFERENCES customers(cus_id),
    FOREIGN KEY (approved_by_employee_id) REFERENCES employees(emp_id)
);
CREATE TABLE IF NOT EXISTS loan_line_items(
	lli_id BIGINT NOT NULL auto_increment,
    loan_id BIGINT NOT NULL,
    lli_processing_date DATETIME NOT NULL,
    lli_effective_date DATETIME NOT NULL,
    lli_type VARCHAR(32),
    lli_status VARCHAR(32),
    lli_amount FLOAT,
    lli_description TEXT,
    lli_pos TEXT,
        
    PRIMARY KEY (lli_id),
    FOREIGN KEY (loan_id) REFERENCES loans(loan_id)   
);
CREATE TABLE IF NOT EXISTS credits(
	credit_id BIGINT NOT NULL auto_increment,
    cus_id BIGINT NOT NULL,
    approved_by_employee_id BIGINT NOT NULL,
    credit_balance FLOAT NOT NULL,
    credit_apr FLOAT,
    credit_type VARCHAR(32),
    credit_credit_score_required INT,
    credit_cash_back FLOAT,
    credit_annual_fee FLOAT,
    credit_late_payment_fee FLOAT,
    credit_over_limit_fee FLOAT,
    
    PRIMARY KEY (credit_id),
    FOREIGN KEY (cus_id) REFERENCES customers(cus_id),
    FOREIGN KEY (approved_by_employee_id) REFERENCES employees(emp_id)
);
CREATE TABLE IF NOT EXISTS credit_line_items(
	cli_id BIGINT NOT NULL auto_increment,
    credit_id BIGINT NOT NULL,
    cli_processing_date DATETIME NOT NULL,
    cli_effective_date DATETIME NOT NULL,
    cli_type VARCHAR(32),
    cli_status VARCHAR(32),
    cli_amount FLOAT,
    cli_description TEXT,
    cli_pos TEXT,
        
    PRIMARY KEY (cli_id),
    FOREIGN KEY (credit_id) REFERENCES credits(credit_id)   
);