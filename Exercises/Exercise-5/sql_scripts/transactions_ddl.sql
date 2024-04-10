CREATE TABLE transactions (
    transaction_id uuid, 
    transaction_date date, 
    product_id int, 
    product_code int, 
    product_description varchar(50), 
    quantity int, 
    account_id int,
    PRIMARY KEY (transaction_id),
    CONSTRAINT fk_products
        FOREIGN KEY(product_id)
            REFERENCES products(product_id),
    CONSTRAINT fk_accounts
        FOREIGN KEY(account_id)
            REFERENCES accounts(customer_id)
);

CREATE INDEX IF NOT EXISTS ix_transactions
ON transactions(transaction_id);