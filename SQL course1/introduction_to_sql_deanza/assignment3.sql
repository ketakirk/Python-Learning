-- Oracle SQL
-- Lab Assignment # 3
-- Your Name: Ketaki Kekatpure
-- Date Handed in: 2/7/2016

-- #1. Write a query to display employee number, employee name, hiredate, manager's name for those employees, whose manager's name starts with K or M or S. Label the columns Employee Number, Employee Name, Hiredate, Mgr Name. 

-- Ans:

SELECT A.empno AS "Employee Number", 
A.ename AS "Employee Name", 
A.hiredate AS "Hiredate", 
B.ename AS "Mgr Name" 
FROM emp A, emp B
WHERE A.mgr = B.empno
AND 
(trim(B.ename) LIKE 'K%' or trim(B.ename) LIKE 'M%' or trim(B.ename) LIKE 'S%');


-- OUTPUT:

-- Employee Number Employee N Hiredate  Mgr Name
-- --------------- ---------- --------- ----------
-- 	   7876 ADAMS	   12-JAN-83 SCOTT
-- 	   7698 BLAKE	   01-MAY-81 KING
-- 	   7782 CLARK	   09-JUN-81 KING
-- 	   7566 JONES	   02-APR-81 KING





-- #2. Create a query that will display the employee name, department number, department name and 
-- all the employees that work in the same department as a given employee. Give each column an appropriate label. 

-- ANS:

SELECT B.ename AS "Employee Name",
A.deptno AS "Dept Number",  
D.dname AS "Dept Name"
FROM emp A, emp B, dept D
WHERE A.ename = 'KING'
AND A.deptno = B.deptno
AND A.deptno = D.deptno;


-- OUTPUT:

-- Employee N Dept Number Dept Name
-- ---------- ----------- --------------
-- KING		    10 ACCOUNTING
-- CLARK		    10 ACCOUNTING
-- MILLER		    10 ACCOUNTING


-- COMMENT: If there are two or more people with the same name (KING) in different departments, this query
-- will display all the people in those departments where employee with the name 'KING' exists.




-- #3. Write a query to display the department name, location of all employees who are clerks. 

-- ANS:

SELECT e.ename, d.dname, d.loc
FROM emp e, dept d
WHERE e.deptno = d.deptno
AND e.job = 'CLERK';


-- OUTPUT:

-- ENAME	   DNAME	  LOC
-- ---------- -------------- -------------
-- MILLER	   ACCOUNTING	  NEW YORK
-- SMITH	   RESEARCH	  DALLAS
-- ADAMS	   RESEARCH	  DALLAS
-- JAMES	   SALES	  CHICAGO





-- #4. Insert a new row into the department table: department number = 50, department name = training, location = San Francisco. Now create a query to display all the employees in department number 20 and 50. Columns to be displayed are emp number, emp name, dept name, dept location. 

-- ANS:

INSERT INTO dept VALUES
(50, 'TRAINING', 'SAN FRANCISCO');
COMMIT;

SELECT e.empno, e.ename, d.dname, d.loc
FROM emp e, dept d
WHERE e.deptno = d.deptno(+)
AND d.deptno IN (20, 50);

-- OUTPUT:

--      EMPNO ENAME      DNAME	     LOC
-- ---------- ---------- -------------- -------------
--       7566 JONES      RESEARCH	     DALLAS
--       7902 FORD       RESEARCH	     DALLAS
--       7369 SMITH      RESEARCH	     DALLAS
--       7788 SCOTT      RESEARCH	     DALLAS
--       7876 ADAMS      RESEARCH	     DALLAS




-- #5. Insert a new row into the emp table - you can choose any values for the fields, but department number should be null. Now create a query to display all the employees and all the departments, using joins.


-- ANS:

INSERT INTO emp2 VALUES 
(7244, 'KIM', 'ANALYST', 7839, '10-JAN-82', 3200, 0, NULL);
COMMIT;

SELECT e.ename, d.dname
FROM emp2 e, dept d
WHERE e.deptno = d.deptno(+)
UNION
SELECT e.ename, d.dname
FROM emp2 e, dept d
WHERE e.deptno(+) = d.deptno;


-- OUTPUT:

-- ENAME	   DNAME
-- ---------- --------------
-- ADAMS
-- ALLEN	   SALES
-- BLAKE	   SALES
-- CLARK	   ACCOUNTING
-- FORD	   RESEARCH
-- JAMES	   SALES
-- JONES	   RESEARCH
-- KIM
-- KING	   ACCOUNTING
-- MARTIN	   SALES
-- MILLER

-- ENAME	   DNAME
-- ---------- --------------
-- SCOTT
-- SMITH	   RESEARCH
-- TURNER	   SALES
-- WARD	   SALES
-- 	   OPERATIONS
-- 	   TRAINING

-- 17 rows selected.
