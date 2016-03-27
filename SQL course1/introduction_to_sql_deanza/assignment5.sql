-- Oracle SQL
-- Lab Assignment # 5
-- Your Name: Ketaki Kekatpure
-- Date Handed in: 2/22/2016


-- Question 1 
-- a. Create a query that displays the employees names and indicates the amounts of their salaries through asterisks. Each asterisk signifies hundred dollars. Sort the data in descending order of salary. Label the column EMPLOYEE_AND_THEIR_SALARIES. 


-- ANS:

SELECT ename, RPAD(' ', round(sal/100, 0), '*') "EMPLOYEE_AND_THEIR_SALARIES"
FROM emp
ORDER BY sal DESC;


-- OUTPUT:


-- ENAME
-- ----------
-- EMPLOYEE_AND_THEIR_SALARIES
-- --------------------------------------------------------------------------------
-- KING
--  *************************************************

-- SCOTT
--  *****************************

-- FORD
--  *****************************


-- ENAME
-- ----------
-- EMPLOYEE_AND_THEIR_SALARIES
-- --------------------------------------------------------------------------------
-- JONES
--  *****************************

-- BLAKE
--  ****************************

-- CLARK
--  ************************


-- ENAME
-- ----------
-- EMPLOYEE_AND_THEIR_SALARIES
-- --------------------------------------------------------------------------------
-- ALLEN
--  ***************

-- TURNER
--  **************

-- MILLER
--  ************


-- ENAME
-- ----------
-- EMPLOYEE_AND_THEIR_SALARIES
-- --------------------------------------------------------------------------------
-- WARD
--  ************

-- MARTIN
--  ************

-- ADAMS
--  **********


-- ENAME
-- ----------
-- EMPLOYEE_AND_THEIR_SALARIES
-- --------------------------------------------------------------------------------
-- JAMES
--  *********

-- SMITH
--  *******


-- 14 rows selected.



-- b. Display the employees name, username, hire date, salary and salary review date, which is the first Monday after six months of service. Label the column REVIEW. Format the dates to appear in the format mm/dd/yy. Salary should be rounded. Username is first two letters of the name in the lower case. 


-- ANS:

SELECT ename AS name, 
LOWER(SUBSTR(ename,1,2)) AS username, 
TO_CHAR(hiredate, 'MM/DD/RR') AS hiredate, 
ROUND(sal, 0) AS salary,
TO_CHAR(NEXT_DAY(ADD_MONTHS(hiredate, 6), 'Monday'), 'MM/DD/RR') AS review
FROM emp;


-- OUTPUT:

-- NAME	   USERNAME HIREDATE	 SALARY REVIEW
-- ---------- -------- -------- ---------- --------
-- KING	   ki	    11/17/81	   5000 05/24/82
-- BLAKE	   bl	    05/01/81	   2850 11/02/81
-- CLARK	   cl	    06/09/81	   2450 12/14/81
-- JONES	   jo	    04/02/81	   2975 10/05/81
-- MARTIN	   ma	    09/28/81	   1250 03/29/82
-- ALLEN	   al	    02/20/81	   1600 08/24/81
-- TURNER	   tu	    09/08/81	   1500 03/15/82
-- JAMES	   ja	    12/03/81	    950 06/07/82
-- WARD	   wa	    02/22/81	   1250 08/24/81
-- FORD	   fo	    12/03/81	   3000 06/07/82
-- SMITH	   sm	    12/17/80	    800 06/22/81

-- NAME	   USERNAME HIREDATE	 SALARY REVIEW
-- ---------- -------- -------- ---------- --------
-- SCOTT	   sc	    12/09/82	   3000 06/13/83
-- ADAMS	   ad	    01/12/83	   1100 07/18/83
-- MILLER	   mi	    01/23/82	   1300 07/26/82

-- 14 rows selected.




-- c. Use subquery to display all employees, in department location 'BOSTON' with a salary of greater than $1000. 


-- ANS:

SELECT ename
FROM emp
WHERE deptno = (SELECT deptno FROM dept WHERE loc IN ('BOSTON'))
AND sal > 1000;

-- OUTPUT:

-- no rows selected




-- Question 2 
-- a. Write a query to display the employee name, job, and hire date for all employees who started between 01/01/81 to 12/31/81. Concatenate the name and job together, separated by a space and comma, and label the column Employees. 


-- ANS:

SELECT TRIM(ename) || ', ' || TRIM(job) AS employees, 
hiredate
FROM emp
WHERE hiredate BETWEEN TO_DATE('01/01/81', 'MM/DD/RR') AND TO_DATE('12/31/81', 'MM/DD/RR');


-- OUTPUT:

-- EMPLOYEES	      HIREDATE
-- --------------------- ---------
-- KING, PRESIDENT       17-NOV-81
-- BLAKE, MANAGER	      01-MAY-81
-- CLARK, MANAGER	      09-JUN-81
-- JONES, MANAGER	      02-APR-81
-- MARTIN, SALESMAN      28-SEP-81
-- ALLEN, SALESMAN       20-FEB-81
-- TURNER, SALESMAN      08-SEP-81
-- JAMES, CLERK	      03-DEC-81
-- WARD, SALESMAN	      22-FEB-81
-- FORD, ANALYST	      03-DEC-81

-- 10 rows selected.



-- b. Explain the usage of correlated subqueries, inline views with an example.


-- ANS:

-- A correlated subquery is a subquery that depends on the outer query for its value. 
-- A correlated subquery can be inefficient as it executes once for every selected row 
-- from the outer query. A correlated subquery can be used in the SELECT, WHERE, and HAVING clauses.

-- Example: In last week's assingment, we wrote a query to display department names 
-- with salary grade, minimum salary and average commission. This is how it would be written as a 
-- correlared subquery:

SELECT ename, empno
FROM emp e 
WHERE comm > (
	SELECT min(NVL(comm,0))
	FROM emp
	WHERE deptno=e.deptno);


-- Inline view creates a subquery in the FROM clause of the SELECT statement. A view is 
-- a virtual table that has characteristics of a table, however, it does not hold actual data. 
-- In an inline view, the subquery is placed after the FROM clause as if it is a table name. 
-- Instead of specifying the table name after the FROM clause, the data actually comes from 
-- a view that is created within the subquery.

-- Example: In last week's assingment, we wrote a query to display department names 
-- with salary grade, minimum salary and average commission. I wrote a inline view query 
-- for this question. Here is the query:

SELECT k.dname, k.minsal, k.avgcom, g.grade
FROM (
	SELECT d.dname, 
	       min(e.sal) as minsal,
		   avg(nvl(e.comm, 0)) as avgcom
	FROM dept d, emp e
	WHERE e.deptno = d.deptno
	GROUP BY dname
	) k, salgrade g
WHERE k.minsal BETWEEN g.losal AND g.hisal;






