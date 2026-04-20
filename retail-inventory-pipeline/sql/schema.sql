CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    product_id INT,
    quantity INT,
    price NUMERIC,
    sale_date DATE
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name TEXT,
    category TEXT
);
