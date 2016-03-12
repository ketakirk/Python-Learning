""" 
Assignment #7 - Part2 Submitted by Ketaki Kekatpure. Course - CS21A
File managerDoc.
Defines class Manager where one object of the class represents one
employee (inherited from the Employee superclass) and additional 
instance variables from the Manager class.
"""

from employee import Employee

class Manager(Employee):
	"""
	One object of this class stores one manager's firstname, lastname,
	SSN and salary, title and bonus.
	"""
	def __init__(self, firstname, lastname, socialSecurity, salary, 
		               title, bonus):
		"""
		Sets firstname, lastname, SSN, salary, title and bonus.
		"""
		Employee.__init__(self, firstname, lastname, socialSecurity, salary)
		self.title = title
		self.bonus = bonus

	def __str__(self):
		"""
		Returns the object's data in a string.
		"""
		return Employee.__str__(self) + "Title: %s\nBonus: %s\n" %\
				(self.title, self.bonus)

"""
Creates one employee and manager object. Calls methods on them for 
testing purposes.
"""

if __name__ == "__main__":
	e1 = Employee("Jane", "Adams", "597-938-9202", 60000)
	print(e1)

	e1.giveRaise(5)
	print(e1)

	m1 = Manager("Joe", "Smith", "657-393-0191", 70000, "Supervisor", 700)
	print(m1)

	m1.giveRaise(10)
	print(m1)


'''---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
OUTPUT

================================ RESTART ================================
>>> 
Firstname: Jane
Lastname: Adams
SSN: 597-938-9202
Salary: 60000

Firstname: Jane
Lastname: Adams
SSN: 597-938-9202
Salary: 63000.0

Firstname: Joe
Lastname: Smith
SSN: 657-393-0191
Salary: 70000
Title: Supervisor
Bonus: 700

Firstname: Joe
Lastname: Smith
SSN: 657-393-0191
Salary: 77000.0
Title: Supervisor
Bonus: 700

>>> 

'''