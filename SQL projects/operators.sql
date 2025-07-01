CREATE TABLE employees (
    id INT,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);


INSERT INTO employees (id, name, department, salary) VALUES
(1, 'Alice', 'HR', 50000),
(2, 'Bob', 'Finance', 60000),
(3, 'Charlie', 'IT', 70000),
(4, 'David', 'Finance', 55000),
(5, 'Eva', 'IT', 72000);

SELECT * FROM employees;

SELECT * FROM employees
WHERE department = 'Finance';

SELECT * FROM employees
WHERE salary > 60000;
