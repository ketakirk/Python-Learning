""" 
Assignment #8 - Part3 Submitted by Ketaki Kekatpure. Course - CS21A
File testDoc.
This file contains all of our "unit tests".
"""

from employee import Employee
from manager import Manager 
import unittest

class TestAssgn(unittest.TestCase):

	def test_giveRaiseE(self):
		e1 = Employee("Adam", "Smith", "123-456-7890", 80000)
		e1.giveRaise(5)
		self.assertEqual(84000, e1.salary, "Failed")

	def test_giveRaiseM(self):
		m1 = Manager("Henry", "George", "987-654-3210", 90000, "PM", 7000)
		m1.giveRaise(5)
		self.assertEqual(94500, m1.salary, "Failed")

	def test_emp_list(self):
		"""
		Contains a list with Employee objects and Manager objects. Uses a 
		loop to give a raise to every object in the list and prints the
		new salary of each employee (along with first name, last name,
		SSN, salary) and title as well as bonus in case of managers. 
		"""
		test_list = [ Employee("Adam", "Smith", "123-456-7890", 80000), 
						Manager("Henry", "George", "987-654-3210", 90000, "PM", 7000), 
						Employee("David", "Gale", "230-654-0987", 40000),
						Manager("John", "Law", "789-456-0123", 25000, "Team Lead", 5000),]

		for ob in test_list:
			ob.giveRaise(10)
			print(ob)


if __name__=='__main__':
	unittest.main()



'''---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
OUTPUT

================================ RESTART ================================
>>> 
Firstname: Adam
Lastname: Smith
SSN: 123-456-7890
Salary: 88000.0

Firstname: Henry
Lastname: George
SSN: 987-654-3210
Salary: 99000.0
Title: PM
Bonus: 7000

Firstname: David
Lastname: Gale
SSN: 230-654-0987
Salary: 44000.0

Firstname: John
Lastname: Law
SSN: 789-456-0123
Salary: 27500.0
Title: Team Lead
Bonus: 5000

...
----------------------------------------------------------------------
Ran 3 tests in 0.348s

OK
>>> 

'''