CREATE TABLE Employees (
  EmployeeID INTEGER,
  FirstName TEXT,
  LastName TEXT,
  Department TEXT,
  Salary INTEGER,
  JoiningDate TEXT  -- Store date as TEXT in 'YYYY-MM-DD' format
);


INSERT INTO Employees (EmployeeID, FirstName, LastName, Department, Salary, JoiningDate) VALUES
(101, 'Alice', 'Johnson', 'HR', 50000.00, '2020-03-15'),
(102, 'Bob', 'Smith', 'Engineering', 75000.00, '2019-06-01'),
(103, 'Charlie', 'Lee', 'Finance', 68000.00, '2021-01-12'),
(104, 'David', 'Brown', 'Engineering', 80000.00, '2018-09-23'),
(105, 'Eve', 'Williams', 'Marketing', 62000.00, '2022-04-17');


SELECT * FROM Employees;


SELECT * FROM Employees
WHERE Salary > 65000;


SELECT * FROM Employees
ORDER BY JoiningDate ASC;


SELECT * FROM Employees
ORDER BY Salary DESC;


SELECT * FROM Employees
WHERE Department = 'Engineering';


UPDATE Employees
SET Salary = Salary * 1.10;

