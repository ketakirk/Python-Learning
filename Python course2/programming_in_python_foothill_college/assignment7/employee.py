""" 
Assignment #7 - Part1 Submitted by Ketaki Kekatpure. Course - CS21A
File employeeDoc.
Defines class Employee where one object of the class represents one
employee.
"""

class Employee:
	"""
	One object of this class stores one employee's firstname, lastname,
	SSN and salary.
	"""
	def __init__(self, firstname, lastname, socialSecurity, salary):
		"""
		Sets firstname, lastname, SSN and salary.
		"""
		self.firstname = firstname
		self.lastname = lastname
		self.socialSecurity = socialSecurity
		self.salary = salary

	def giveRaise(self, percentRaise):
		"""
		Takes float "percentRaise" as parameter. This method adds "percentRaise"
		percent of the current salary to the salary instance variable of the 
		object and calls it, providing the value of the new salary based on the 
		raise.
		"""
		self.salary = (self.salary * percentRaise/100) + self.salary

	def __str__(self):
		"""
		Returns the object's data in a string.
		"""
		return "Firstname: %s\nLastname: %s\nSSN: %s\nSalary: %s\n" %\
				(self.firstname, self.lastname, self.socialSecurity, self.salary)

"""
Creates two Employee objects and calls methods on them for testing purposes.
"""
if __name__ == "__main__":
	employee1 = Employee("Mickey", "Mouse", "597-938-9202", 60000)
	print(employee1)

	employee2 = Employee("Donald", "Duck", "597-938-0002", 70000)
	print(employee2)

	employee1.giveRaise(10)
	print(employee1)

	employee2.giveRaise(15)
	print(employee2)


'''---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
OUTPUT

================================ RESTART ================================
>>> 
Firstname: Mickey
Lastname: Mouse
SSN: 597-938-9202
Salary: 60000

Firstname: Donald
Lastname: Duck
SSN: 597-938-0002
Salary: 70000

Firstname: Mickey
Lastname: Mouse
SSN: 597-938-9202
Salary: 66000.0

Firstname: Donald
Lastname: Duck
SSN: 597-938-0002
Salary: 80500.0

>>> 

'''

