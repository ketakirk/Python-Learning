-- Oracle SQL
-- Lab Assignment # 7
-- Your Name: Ketaki Kekatpure
-- Date Handed in: 3/20/2016



-- Q1. Create Table and Tablespaces  Q1. Based on the schema in Lab 6, 
-- create tables with  constraints. Consider using the following constraints 
-- as appropriate Primary Key, Foreign key, Unique, Null or Check. 


--echo Building demo tables. Please wait.
DROP TABLE college CASCADE CONSTRAINTS;
DROP TABLE dept CASCADE CONSTRAINTS;
DROP TABLE course CASCADE CONSTRAINTS;
DROP TABLE location CASCADE CONSTRAINTS;
DROP TABLE user CASCADE CONSTRAINTS;
DROP TABLE section CASCADE CONSTRAINTS;
DROP TABLE payment CASCADE CONSTRAINTS;
DROP TABLE resident;
DROP TABLE studentregistration;

CREATE TABLESPACE user_local_database DATAFILE 'cld_f1.dbf' SIZE 500M
EXTENT MANAGEMENT LOCAL AUTOALLOCATE;

CREATE TABLE college(
collegeid NUMBER(5) NOT NULL,
collegename VARCHAR2(50),
address VARCHAR2(250) NOT NULL,
telno VARCHAR2(15) NOT NULL,
CONSTRAINT college_collegeid_pk PRIMARY KEY (collegeid),
CONSTRAINT college_collegename_uk UNIQUE (collegename));

CREATE TABLE dept (
deptid NUMBER(5) NOT NULL,
deptname VARCHAR2(50),
collegeid NUMBER(5) NOT NULL,
locationid NUMBER(5) NOT NULL,
CONSTRAINT dept_deptid_pk PRIMARY KEY (deptid),
CONSTRAINT dept_collegeid_fk FOREIGN KEY (collegeid)
	REFERENCES college (collegeid),
CONSTRAINT dept_locationid_fk FOREIGN KEY (locationid)
	REFERENCES location (locationid));

CREATE TABLE course (
courseid NUMBER(5) NOT NULL,
courseno VARCHAR2(10),
coursename VARCHAR2(50) NOT NULL,
prerequisite VARCHAR2(100),
deptid NUMBER(5) NOT NULL,
CONSTRAINT course_courseid_pk PRIMARY KEY (courseid),
CONSTRAINT course_deptid_fk FOREIGN KEY (deptid)
	REFERENCES dept (deptid));

CREATE TABLE location (
locationid NUMBER(5) NOT NULL,
locationname VARCHAR2(250) NOT NULL,
CONSTRAINT location_locationid_pk PRIMARY KEY (locationid));

CREATE TABLE user (
userid NUMBER(10) NOT NULL,
firstname VARCHAR2(50) NOT NULL,
lastname VARCHAR2(50) NOT NULL,
address VARCHAR2(250) NOT NULL,
email VARCHAR2(100),
telno VARCHAR2(15),
residentid NUMBER(5) NOT NULL,
type CHAR(1) NOT NULL,
CONSTRAINT user_userid_pk PRIMARY KEY (userid),
CONSTRAINT user_residentid_fk FOREIGN KEY (residentid)
	REFERENCES resident (residentid));

CREATE TABLE section (
sectionid NUMBER(5) NOT NULL,
sectionno CHAR(10),
courseid NUMBER(5) NOT NULL,
locationid NUMBER(5) NOT NULL,
starttime DATE NOT NULL,
endtime DATE NOT NULL,
startdate DATE NOT NULL,
enddate DATE NOT NULL,
userid NUMBER(10) NOT NULL,
CONSTRAINT section_sectionid_pk PRIMARY KEY (sectionid),
CONSTRAINT section_courseid_fk FOREIGN KEY (courseid)
	REFERENCES course (courseid),
CONSTRAINT section_locationid_fk FOREIGN KEY (locationid)
	REFERENCES location (locationid),
CONSTRAINT section_userid_fk FOREIGN KEY (userid),
	REFERENCES user (userid));

CREATE TABLE payment (
paymentid NUMBER(5) NOT NULL,
paymentname ENUM('visa', 'cash', 'mc') CONSTRAINT payment_paymentname_ck
	CHECK(paymentname in ('visa', 'cash', 'mc'),
CONSTRAINT payment_paymentid_pk PRIMARY KEY (paymentid));
# ENUM is outside the allowed types for this assignment, however, 
# I wanted to know if this would be the right type to use if available.
# I have used paymentname (visa - 1, mc - 2, cash - 3) - CHAR(1) in assignment 6.

CREATE TABLE resident (
residentid NUMBER(5) NOT NULL,
resiname CHAR(1) CONSTRAINT resident_resiname_ck
	CHECK(resiname in ('r', 'n'),
feeschedule NUMBER(5) NOT NULL,
CONSTRAINT resident_residentid_pk PRIMARY KEY (residentid));

CREATE TABLE studentregistration (
studentregid NUMBER(10) NOT NULL,
studentid NUMBER(10) NOT NULL,
sectionid NUMBER(5) NOT NULL,
feestatus CHAR(10) NOT NULL,
paymentid NUMBER(5) NOT NULL,
CONSTRAINT studentregistration_studentregid_pk PRIMARY KEY (studentregid),
CONSTRAINT studentregistration_studentid_fk FOREIGN KEY (studentid)
	REFERENCES user (userid),
CONSTRAINT studentregistration_sectionid_fk FOREIGN KEY (sectionid)
	REFERENCES section (sectionid),
CONSTRAINT studentregistration_paymentid_fk FOREIGN KEY (paymentid)
	REFERENCES payment (paymentid));


COMMIT;

-- Q2. Project which tables will increase quickly and implement partitioning 
-- types in at least 2 tables in your schema. Explain why these partitioning 
-- types would be useful in the context of your implementation. 

-- I believe the user and the section tables will increase quickly. The range partition 
-- will make it easier to search for sections according to the quarters (Winter, Spring, 
-- Summer and Fall) in which the courses were offered. The range partition will also help
-- to search for users according to their user ids.


CREATE TABLE user (
userid NUMBER(10) NOT NULL,
firstname VARCHAR2(50) NOT NULL,
lastname VARCHAR2(50) NOT NULL,
address VARCHAR2(250) NOT NULL,
email VARCHAR2(100),
telno VARCHAR2(15),
residentid NUMBER(5) NOT NULL,
type CHAR(1) NOT NULL,
CONSTRAINT user_userid_pk PRIMARY KEY (userid),
CONSTRAINT user_residentid_fk FOREIGN KEY (residentid)
	REFERENCES resident (residentid)
PARTITION BY RANGE(userid)
(PARTITION u1 VALUES LESS THAN (25000000) TABLESPACE us1),
(PARTITION u2 VALUES LESS THAN (50000000) TABLESPACE us2),
(PARTITION u3 VALUES LESS THAN (75000000) TABLESPACE us3),
(PARTITION u4 VALUES LESS THAN (MAXVALUE) TABLESPACE us4));



CREATE TABLE section (
sectionid NUMBER(5) NOT NULL,
sectionno CHAR(10),
courseid NUMBER(5) NOT NULL,
locationid NUMBER(5) NOT NULL,
starttime DATE NOT NULL,
endtime DATE NOT NULL,
startdate DATE NOT NULL,
enddate DATE NOT NULL,
userid NUMBER(10) NOT NULL,
CONSTRAINT section_sectionid_pk PRIMARY KEY (sectionid),
CONSTRAINT section_courseid_fk FOREIGN KEY (courseid)
	REFERENCES course (courseid),
CONSTRAINT section_locationid_fk FOREIGN KEY (locationid)
	REFERENCES location (locationid),
CONSTRAINT section_userid_fk FOREIGN KEY (userid),
	REFERENCES user (userid))

PARTITION BY RANGE(startdate)
(PARTITION WINTER_Q1_2016 VALUES LESS THAN (TO_DATE('25-MAR-2016', 'DD-MON-YYYY')),
(PARTITION SPRING_Q2_2016 VALUES LESS THAN (TO_DATE('25-JUN-2016', 'DD-MON-YYYY')),
(PARTITION SUMMER_Q3_2016 VALUES LESS THAN (TO_DATE('25-AUG-2016', 'DD-MON-YYYY')),
(PARTITION FALL_Q4_2016 VALUES LESS THAN (TO_DATE('25-NOV-2016', 'DD-MON-YYYY')));


