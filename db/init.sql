-- Example SQL script to initialize the database
CREATE TABLE my_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    value INTEGER
);

INSERT INTO my_table (name, value) VALUES
('Alice', 10),
('Bob', 20),
('Charlie', 30);