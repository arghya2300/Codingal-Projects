CREATE TABLE IF NOT EXISTS employees (
    id INT PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INT
);

INSERT INTO employees (id, name, department, salary) VALUES
(1, 'Alice', 'Engineering', 70000),
(2, 'Bob', 'Engineering', 80000),
(3, 'Charlie', 'HR', 50000),
(4, 'Diana', 'HR', 52000),
(5, 'Evan', 'Sales', 45000),
(6, 'Fiona', 'Sales', 47000),
(7, 'George', 'Engineering', 85000),
(8, 'Hannah', 'Marketing', 60000);

SELECT 
    SUM(salary) AS total_salary
FROM 
    employees;

SELECT 
    AVG(salary) AS average_salary
FROM 
    employees;

SELECT 
    department,
    COUNT(*) AS total_employees
FROM 
    employees
GROUP BY 
    department;

SELECT 
    MIN(salary) AS minimum_salary,
    MAX(salary) AS maximum_salary
FROM 
    employees;

SELECT 
    department,
    SUM(salary) AS total_dept_salary,
    AVG(salary) AS avg_dept_salary,
    MIN(salary) AS min_dept_salary,
    MAX(salary) AS max_dept_salary
FROM 
    employees
GROUP BY 
    department;
