-- Oracle SQL
-- Lab Assignment # 4
-- Your Name: Ketaki Kekatpure
-- Date Handed in: 2/10/2016


-- #1. Display the manager number and the salary of the lowest paid employee for that manager. Exclude anyone whose manager is not known. Exclude any groups where the minimum salary is less than $1000. Sort the output in descending order of salary. 

-- ANS:

SELECT mgr, min(sal) AS msal
FROM emp
WHERE mgr IS NOT NULL
GROUP BY mgr
HAVING MIN(sal) >= 1000
ORDER BY msal DESC;


-- OUTPUT:

--        MGR	 MSAL
-- ---------- ----------
--       7566	 3000
--       7839	 2450
--       7782	 1300
--       7788	 1100



-- #2. Write a query to display the department name, location name, number of employees, and the average salary for all employees in that department. Label the columns dname, loc, Number of People, and Salary, respectively. 

-- ANS:

SELECT d.dname, d.loc, 
COUNT(e.sal) AS "Number of People", 
AVG(e.sal) AS "SALARY"
FROM dept d, emp e
WHERE d.deptno = e.deptno
GROUP BY d.dname, d.loc;


-- OUTPUT:

-- DNAME	       LOC	     Number of People	  SALARY
-- -------------- ------------- ---------------- ----------
-- ACCOUNTING     NEW YORK 		    3 2916.66667
-- SALES	       CHICAGO			    6 1566.66667
-- RESEARCH       DALLAS			    5	    2175



-- #3. Write a query to display department names with salary grade, minimum salary and average commission. For departments with null commission, you should display 0. (salgrade table can be used for getting salary grade). 


-- ANS:

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


-- OUTPUT:

-- DNAME		   MINSAL     AVGCOM	  GRADE
-- -------------- ---------- ---------- ----------
-- ACCOUNTING	     1300	   0	      2
-- SALES		      950 366.666667	      1
-- RESEARCH	      800	   0	      1



-- #4. What is difference between COUNT(*), COUNT(col_name), COUNT(DISTINCT(col_name)), COUNT(ALL(col_name))? Explain with examples. 


-- ANS: 

COUNT(*) is used to determine the number of rows in a given table. The result includes redundant rows and rows containing Null values. The COUNT(*) query on the emp table displays the total number of employee records in the emp table and gives 14 as the result.
Example: Query:

SELECT COUNT(*) FROM emp;


OUTPUT:

  COUNT(*)
----------
	14


COUNT(col_name) gives the total number of non-NULL values in a given column. COUNT(col_name) treats duplicate records as unique and includes them in the final count. The COUNT(mgr) query displays the total number of managers in the mgr column. As one of the employees, "King", does not have a manager, the result is 13.
Example: Query:

SELECT COUNT(mgr) FROM emp;

OUTPUT:

COUNT(MGR)
----------
	13


COUNT(DISTINCT(col_name)) displays the unique number of non-Null values in a given column. It does not count duplicate records. So, if we consider our previous example, DISTINCT will display the total number of unique managers in the mgr column.
Example: Query:

SELECT COUNT(DISTINCT(mgr)) FROM emp;

OUTPUT:

COUNT(DISTINCT(MGR))
--------------------
		   6


COUNT(ALL(col_name)) is the same as COUNT(col_name). It displays the total number of non-NULL values in a given column.

SELECT COUNT(ALL(mgr)) FROM emp;

OUTPUT:

COUNT(ALL(MGR))
---------------
	     13



-- #5. Display the employee number, name, salary, and salary increase by 15% expressed as a whole number. Label the column New Salary. 

-- ANS:

SELECT empno, ename, sal, 
ROUND(sal + (sal * 15)/100) AS "New Salary"
FROM emp;


-- OUTPUT:

--      EMPNO ENAME	     SAL New Salary
-- ---------- ---------- ---------- ----------
--       7839 KING 	    5000       5750
--       7698 BLAKE	    2850       3278
--       7782 CLARK	    2450       2818
--       7566 JONES	    2975       3421
--       7654 MARTIN	    1250       1438
--       7499 ALLEN	    1600       1840
--       7844 TURNER	    1500       1725
--       7900 JAMES	     950       1093
--       7521 WARD 	    1250       1438
--       7902 FORD 	    3000       3450
--       7369 SMITH	     800	920

--      EMPNO ENAME	     SAL New Salary
-- ---------- ---------- ---------- ----------
--       7788 SCOTT	    3000       3450
--       7876 ADAMS	    1100       1265
--       7934 MILLER	    1300       1495

-- 14 rows selected.

