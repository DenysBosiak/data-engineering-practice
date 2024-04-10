CREATE TABLE products (
    product_id int, 
    product_code int, 
    product_description varchar(50),
    PRIMARY KEY (product_id)
);

CREATE INDEX IF NOT EXISTS ix_products
ON products(product_id, product_code);