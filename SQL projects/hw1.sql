
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(100)
);

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    customer_id INT,
    product_name VARCHAR(100),
    export_country VARCHAR(100),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

INSERT INTO Customers (customer_id, name, country) VALUES
(1, 'Alice', 'USA'),
(2, 'Aaron', 'Canada'),
(3, 'George', 'UK'),
(4, 'Dorothy', 'Australia'),
(5, 'Lora', 'India'),
(6, 'Arjun', 'India');

INSERT INTO Products (product_id, customer_id, product_name, export_country) VALUES
(1, 1, 'Laptop', 'Germany'),
(2, 2, 'Tablet', 'USA'),
(3, 3, 'Monitor', 'France'),
(4, 4, 'Keyboard', 'UK'),
(5, 5, 'Mouse', 'Germany'),
(6, 6, 'Phone', 'USA');

SELECT * 
FROM Customers
WHERE name LIKE 'a%';

SELECT * 
FROM Customers
WHERE name LIKE '%or%';

SELECT * 
FROM Customers
WHERE name LIKE 'a%' OR name LIKE '%or%';

SELECT DISTINCT 
    c.name AS customer_name,
    p.product_name,
    p.export_country
FROM Customers c
JOIN Products p ON c.customer_id = p.customer_id
WHERE c.name LIKE 'a%' OR c.name LIKE '%or%';

SELECT 
    c.name AS customer_name,
    COUNT(p.product_id) AS total_products
FROM Customers c
JOIN Products p ON c.customer_id = p.customer_id
WHERE c.name LIKE 'a%' OR c.name LIKE '%or%'
GROUP BY c.name;

SELECT 
    c.name AS customer_name,
    GROUP_CONCAT(DISTINCT p.export_country) AS export_countries
FROM Customers c
JOIN Products p ON c.customer_id = p.customer_id
WHERE c.name LIKE 'a%' OR c.name LIKE '%or%'
GROUP BY c.name;

