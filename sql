
CREATE DATABASE company;
USE company;

CREATE TABLE Department (
    DeptNo INT PRIMARY KEY,
    DeptName VARCHAR(30) NOT NULL,
    Location VARCHAR(30)
);

CREATE TABLE Employee1 (
    EmpID INT,
    EmpName VARCHAR(50),
    DeptID INT,
    Salary DECIMAL(10,2)
);

CREATE TABLE Staff (
    EmpID INT,
    EmpName VARCHAR(50),
    DeptID INT,
    Salary DECIMAL(10,2)
);

INSERT INTO Staff (EmpID, EmpName, DeptID, Salary) VALUES
(4, 'David', 104, 52000),
(5, 'Eva', 105, 58000),
(2, 'Bob', 102, 60000),      -- duplicate across tables
(5, 'Eva', 105, 58000);      -- duplicate within this table


INSERT INTO Employee1 (EmpID, EmpName, DeptID, Salary) VALUES
(1, 'Alice', 101, 50000),
(2, 'Bob', 102, 60000),
(3, 'Charlie', 103, 55000),
(2, 'Bob', 102, 60000),      -- duplicate row
(1, 'Alice', 101, 50000) ,  -- duplicate row
(4,'lee',104,65000);


CREATE TABLE Employee (
    FName VARCHAR(15) NOT NULL,
    MidName CHAR(2),
    LName VARCHAR(15) NOT NULL,
    SSN CHAR(9) PRIMARY KEY,
    BDate DATE,
    Address VARCHAR(50),
    Sex CHAR(1) CHECK (Sex IN ('M', 'F', 'm', 'f')),
    Salary DECIMAL(7,2) DEFAULT 800,
    SuperSSN CHAR(9),
    DeptNo INT,
    CONSTRAINT fk_dept FOREIGN KEY (DeptNo) REFERENCES Department(DeptNo)
);

INSERT INTO Department (DeptNo, DeptName, Location)
VALUES
(1, 'HR', 'New York'),
(2, 'Finance', 'Chicago'),
(3, 'IT', 'San Francisco');

INSERT INTO Employee (FName, MidName, LName, SSN, BDate, Address, Sex, Salary, SuperSSN, DeptNo)
VALUES
('John', 'A', 'Smith', '123456789', '1985-05-15', '123 Main St', 'M', 5000.00, NULL, 1),
('Jane', 'B', 'Doe', '987654321', '1990-08-22', '456 Oak St', 'F', 6000.00, '123456789', 2),
('Mike', NULL, 'Johnson', '555666777', '1992-11-10', '789 Pine St', 'M', 4500.00, '987654321', 3);

-- duplicates
-- INSERT INTO Employee (FName, MidName, LName, SSN, BDate, Address, Sex, Salary, SuperSSN, DeptNo)
-- VALUES
-- ('John', 'A', 'Smith', '123456780', '1985-05-15', '123 Main St', 'M', 5000.00, NULL, 1),
-- ('John', 'A', 'Smith', '123456781', '1985-05-15', '123 Main St', 'M', 5000.00, NULL, 1);

select * from Employee;

select * from department;

start transaction;

savepoint a;

delete from employee where deptno = 3;

rollback to a;

-- no rollback

truncate table employee;   

drop table employee;

-- Joins

select d.deptName,d.location , e.Fname,e.MidName,e.Lname,e.ssn,e.Bdate,e.Address,e.sex ,e.salary from department d join  Employee e on d.deptno=e.deptno;

select d.deptName,d.location , e.Fname,e.MidName,e.Lname,e.ssn,e.Bdate,e.Address,e.sex ,e.salary from department d left join Employee e on  d.deptno=e.deptno;

select d.deptName,d.location , e.Fname,e.MidName,e.Lname,e.ssn,e.Bdate,e.Address,e.sex ,e.salary from department d right join Employee e on  d.deptno=e.deptno;

-- select d.deptName,d.location , e.Fname,e.MidName,e.Lname,e.ssn,e.Bdate,e.Address,e.sex ,e.salary from department d outer join Employee e on  d.deptno=e.deptno;

select d.deptName,d.location , e.Fname,e.MidName,e.Lname,e.ssn,e.Bdate,e.Address,e.sex ,e.salary from department d cross join Employee e on  d.deptno=e.deptno;

commit;

-- without duplicate 
select * from employee1 
union 
select * from staff; 


-- with duplicate
select * from employee1 
union all
select * from staff; 

-- window function
-- normal

select empid,empname,deptid,avg(salary) as avg_sal from employee1 group by deptid; -- if we didn't add these in group by empid,empname it will give error;

select deptid,avg(salary) as avg_sal from employee1 group by deptid;

select empid,empname,deptid,
avg(salary) over(partition by deptid) as avg
from employee1;


-- row_num()
select empid,empname,deptid,
ROW_NUMBER() over(partition by deptid order by empid) as rn
from employee1;
-- o/p 1 2 1 2 1 1

INSERT INTO employee1 VALUES (5, 'Sam', 102, 55000.00);
INSERT INTO employee1 VALUES (6, 'John', 102, 55000.00);


-- rank()
SELECT 
    EmpID,
    EmpName,
    DeptID,
    Salary,

    -- Row Numbering & Ranking
    ROW_NUMBER() OVER (PARTITION BY DeptID ORDER BY Salary DESC) AS RowNumInDept,
    RANK()       OVER (PARTITION BY DeptID ORDER BY Salary DESC) AS RankInDept,
    DENSE_RANK() OVER (PARTITION BY DeptID ORDER BY Salary DESC) AS DenseRankInDept,

    -- Running Aggregates
    SUM(Salary) OVER (PARTITION BY DeptID ORDER BY Salary DESC) AS RunningTotal,
    AVG(Salary) OVER (PARTITION BY DeptID ORDER BY Salary DESC) AS RunningAverage,

    -- Previous & Next Value
    LAG(Salary, 1)  OVER (PARTITION BY DeptID ORDER BY Salary DESC) AS PrevSalary,
    LEAD(Salary, 1) OVER (PARTITION BY DeptID ORDER BY Salary DESC) AS NextSalary,
	NTILE(2)      OVER (PARTITION BY DeptID ORDER BY Salary DESC) AS NtileGroup
FROM employee1;

-- Aggregate 

SELECT DeptID,
       SUM(Salary) AS Total_Salary,
       AVG(Salary) AS Avg_Salary,
       MIN(Salary) AS Min_Salary,
       MAX(Salary) AS Max_Salary,
       COUNT(*) AS Num_Employees,
       VAR_POP(Salary) AS Var_Pop,
       VAR_SAMP(Salary) AS Var_Samp,
       STDDEV_POP(Salary) AS StdDev_Pop,
       STDDEV_SAMP(Salary) AS StdDev_Samp
FROM employee1
GROUP BY DeptID;

-- . Value Functions
SELECT 
    EmpID,
    EmpName,
    DeptID,
    Salary,
    
    -- Previous salary in the same department
    LAG(Salary, 1, 0) OVER (PARTITION BY DeptID ORDER BY Salary DESC) AS PrevSalary,
    
    -- Next salary in the same department
    LEAD(Salary, 1, 0) OVER (PARTITION BY DeptID ORDER BY Salary DESC) AS NextSalary,
    
    -- Highest salary in the department
    FIRST_VALUE(Salary) OVER (PARTITION BY DeptID ORDER BY Salary DESC) AS HighestInDept,
    
    -- Lowest salary in the department
    LAST_VALUE(Salary) OVER (
        PARTITION BY DeptID 
        ORDER BY Salary DESC 
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS LowestInDept,
    
    -- 2nd highest salary in the department
    NTH_VALUE(Salary, 2) OVER (PARTITION BY DeptID ORDER BY Salary DESC 
                               ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS SecondHighestInDept

FROM employee1
ORDER BY DeptID, Salary DESC;



-- Analytic/Navigation Functions
SELECT EmpID, EmpName, DeptID, Salary,
       PERCENT_RANK() OVER (PARTITION BY DeptID ORDER BY Salary) AS pct_rank,
       CUME_DIST()   OVER (PARTITION BY DeptID ORDER BY Salary) AS cum_dist
FROM employee1
ORDER BY DeptID, Salary DESC;

select * from department;
-- substring
select empname,substring(empname,1,3) as 3a from employee1;

-- concat
select CONCAT(DeptName,'',DeptNo) from department;  -- only in mysql works function concat() works plsql ||''|| or + -works

-- locate
SELECT 
    location,
    SUBSTRING(location, 1, LOCATE(' ', location) - 1) AS first_part
FROM department
WHERE LOCATE(' ', location) > 0; -- only when space is available in the location

--
SELECT 
    EmpID,
    EmpName,
    -- LEFT: first 2 letters of name
    LEFT(EmpName, 2) AS FirstTwoChars,
    
    -- RIGHT: last 2 letters of name
    RIGHT(EmpName, 2) AS LastTwoChars,
    
    -- LENGTH: length of name
    LENGTH(EmpName) AS NameLength,
    
    -- LOCATE: find position of 'a' in name
    LOCATE('a', EmpName) AS PositionOfA,
    
    -- CONCAT: combine name with salary
    CONCAT(EmpName, ' earns ', Salary) AS NameWithSalary,
    
    -- REPLACE: replace 'a' with 'x' in name
    REPLACE(EmpName, 'a', 'x') AS NameReplaced
FROM Employee1;
--
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerName VARCHAR(50),
    Product VARCHAR(50),
    OrderDate DATE,
    Quantity INT,
    Price DECIMAL(10,2)
);
INSERT INTO Orders (OrderID, CustomerName, Product, OrderDate, Quantity, Price) VALUES
(1, 'Alice', 'Laptop',    '2025-01-15', 1, 60000.00),
(2, 'Bob',   'Mouse',     '2025-02-10', 2, 1500.00),
(3, 'Charlie','Keyboard', '2025-02-25', 1, 3000.00),
(4, 'Alice', 'Monitor',   '2025-03-05', 2, 12000.00),
(5, 'Eve',   'Laptop',    '2025-03-15', 1, 65000.00),
(6, 'Frank', 'Headset',   '2025-04-02', 3, 2500.00),
(7, 'Bob',   'Laptop',    '2025-05-20', 1, 62000.00),
(8, 'Charlie','Mouse',    '2025-06-01', 4, 1400.00),
(9, 'Alice', 'Keyboard',  '2025-06-18', 1, 3200.00),
(10,'Eve',   'Monitor',   '2025-07-22', 2, 12500.00);

-- intervals time
select orderid,customername,timestampdiff(day,OrderDate,curdate()) as dob from  orders; -- 3 arg required

-- nvl()
INSERT INTO Orders (OrderID, CustomerName, Product, OrderDate, Quantity, Price) VALUES
(11, NULL, 'Laptop',    '2025-08-01', 1, 60000.00),   -- NULL customer
(12, 'George', NULL,    '2025-08-05', 2, 1500.00),   -- NULL product
(13, 'Helen', 'Mouse',  NULL,          3, 1400.00),   -- NULL order date
(14, 'Ivy',   'Monitor','2025-08-10', NULL, 12500.00),-- NULL quantity
(15, 'Jack',  'Keyboard','2025-08-15', 2, NULL);      -- NULL price

select * from orders;

select orderid,ifnull(CustomerName,'eee') as dfdj from orders; -- NVL()/ifnull

-- COALESCE()

select orderid, coalesce(customername,product) as ex from orders;-- non null value

select orderid,coalesce(CustomerName,'eee') as dfdj from orders; -- supports nvl()/if null function also

-- wildcards()
select * from orders;

select * from orders where customername like '%e';
select * from orders where customername like '_v%';

-- regrex

select * from orders where customername REGEXP '^[aeiouAEIOU]'; -- 

select * from orders where customername REGEXP '^[^AEIOU]'--;

SELECT 
    OrderID,
    CustomerName,
    -- ^ : starts with A
    CustomerName REGEXP '^A' AS starts_with_A,
    -- $ : ends with e
    CustomerName REGEXP 'e$' AS ends_with_e,
    -- . : second character is 'a'
    CustomerName REGEXP '^.a' AS second_char_a,
    -- [abc] : starts with a, b, or c
    CustomerName REGEXP '^[abcABC]' AS starts_with_abc,
    -- [^abc] : does NOT start with a, b, or c
    CustomerName REGEXP '^[^abcABC]' AS not_starts_with_abc,
    -- [a-z] : starts with lowercase letter
    CustomerName REGEXP '^[a-z]' AS starts_lowercase,
    -- * : zero or more 'a'
    CustomerName REGEXP 'a*' AS has_zero_or_more_a,
    -- + : one or more 'a'
    CustomerName REGEXP 'a+' AS has_one_or_more_a,
    -- {2} : exactly 2 consecutive 'a'
    CustomerName REGEXP 'a{2}' AS has_double_a,
    -- {2,} : at least 2 consecutive 'a'
    CustomerName REGEXP 'a{2,}' AS has_two_or_more_a,
    -- {1,3} : between 1 and 3 consecutive 'a'
    CustomerName REGEXP 'a{1,3}' AS has_between_one_and_three_a
FROM Orders;

-- Index 


select * from orders;

create index idx_orderid on orders(orderid);

drop index idx_orderid on orders;

-- view

create view kk as 
select * from orders;

update kk set price = 555555 where orderid=14;

drop view kk;


