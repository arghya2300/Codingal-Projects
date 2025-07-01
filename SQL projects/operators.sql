CREATE TABLE customers (
    id INT,
    name VARCHAR(50),
    city VARCHAR(50),
    grade INT
);


INSERT INTO customers (id, name, city, grade) VALUES
(1, 'Alice', 'New York', 120),
(2, 'Bob', 'Chicago', 110),
(3, 'Charlie', 'New York', 90),
(4, 'David', 'Houston', 80),
(5, 'Eva', 'New York', 130),
(6, 'Frank', 'Dallas', 105);


SELECT * FROM customers
WHERE city = 'New York';


SELECT * FROM customers
WHERE grade > 100;


SELECT * FROM customers
WHERE city = 'New York' AND grade > 100;


SELECT * FROM customers
WHERE city = 'New York' OR grade > 100;
