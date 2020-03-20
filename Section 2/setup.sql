CREATE TABLE salespersons (
    id SERIAL PRIMARY KEY,
    name varchar(255) NOT NULL
);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name_ char(50) NOT NULL,
    phone_number char(50) NOT NULL
);

CREATE TABLE cars (
    id SERIAL PRIMARY KEY,
    manufacturer char(50) NOT NULL,
    model_name char(50) NOT NULL,
    model_variant char(50) NOT NULL,
    serial_number char(50) NOT NULL,
    weight_ int NOT NULL,
    engine_cc int NOT NULL,
    price int NOT NULL,
    is_used boolean NOT NULL
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    salesperson_id int REFERENCES salespersons(id) NOT NULL,
    customer_id int REFERENCES customers(id) NOT NULL,
    car_id int REFERENCES cars(id) NOT NULL,
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);