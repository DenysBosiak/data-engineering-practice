CREATE TABLE accounts (
    customer_id int, 
    first_name varchar(50), 
    last_name varchar(50), 
    address_1 varchar(50), 
    address_2 varchar(50), 
    city varchar(50), 
    state varchar(50), 
    zip_code int, 
    join_date date,
    PRIMARY KEY (customer_id)
);

CREATE INDEX IF NOT EXISTS ix_account
ON accounts(customer_id);