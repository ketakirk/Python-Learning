-- Oracle SQL
-- Lab Assignment # 8
-- Your Name: Ketaki Kekatpure
-- Date Handed in: 3/22/2016


-- Based on Lab 7. 

-- Write DML Statements to simulate the following Business Processes:
-- 1. Setup a department, course within a department with 2 sections. 
-- 	Section must have a location assigned. Produce a report showing 
-- 	the department, its course and sections (with complete section information.)

INSERT INTO college VALUES
(050, 'SAMPLE COLLEGE', 'SAN FRANCISCO', '95050');

INSERT INTO dept VALUES
(00234, 'INFORMATION SYSTEMS', 050, 3490);

INSERT INTO course VALUES
(5555, 'AA229', 'INTRO TO SYSTEMS', 'INTRO TO CS', 00234);

INSERT INTO location VALUES
(3490, 'BLDG 3');

INSERT INTO section VALUES
(4005, 'A1', 5555, 3490, '11:00:00', '12:30:00', '10-APR-2016', '10-JUN-2016', 12345678);
INSERT INTO section VALUES
(4006, 'A2', 5555, 3490, '16:00:00', '17:30:00', '10-APR-2016', '10-JUN-2016', 87654321);

COMMIT;


-- REPORT

SELECT d.deptname, c.coursename, s.*
FROM dept d, course c, section s
WHERE d.deptid = c.deptid AND c.courseid = s.courseid;



-- 2. Now register a student to a section and process student payment. Produce a 
--  	report showing student registration information, including payment information.

INSERT INTO user VALUES
(12345678, 'Jane', 'Adams', 'Santa Clara', NULL, NULL, 6590, 'r');

INSERT INTO payment VALUES
(450, 'visa');

INSERT INTO resident VALUES
(6590, 'r', 18);

INSERT INTO studentregistration VALUES
(1134, 12345678, 4005, 'Paid', 450);

COMMIT;

SELECT u.firstname, u.lastname, p.*, s.*
FROM payment p, studentregistration s, user u
WHERE u.userid = s.studentid AND p.paymentid = s.paymentid;


-- How can you improve your DB Schema further. Make four recommendations.

-- Based on the feedback that you provided on the previous assignment and while 
-- working on question 2 of this assignment, I realized that I did not provide 
-- partitions to the student registration and payment tables in my last assignment. 
-- I would make those two changes to my schema.

-- Other than that, I would explore other data types. For example: In the user table, 
-- for the resident 'type' field, I would use ENUM data type to avoid errors caused 
-- by humans while entering data. 
