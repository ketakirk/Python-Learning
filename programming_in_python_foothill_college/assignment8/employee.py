""" 
Assignment #8 - Part1 Submitted by Ketaki Kekatpure. Course - CS21A
File employeeDoc.
Defines class Employee where one object of the class represents one
employee.
"""
from functools import total_ordering

@total_ordering
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

	def __eq__(self, other):
		"""
		Returns True if firstname and the lastname in the two objects (self and 
		other) are same, otherwise it returns False. 
		"""
		print("First object is ", self.firstname, self.lastname, 
			"\nSecond object is ", other.firstname, other.lastname)
		return self.firstname == other.firstname and self.lastname == other.lastname

	def __lt__(self, other):
		"""
		Returns True when the name in self is alphabetically less than the name in
		other. If the last names are equal, the method checks the first names to 
		determine which object is less than the other. 
		"""

		if self.lastname.lower() < other.lastname.lower():
			return True
		elif self.lastname.lower() > other.lastname.lower():
			return False
		elif self.lastname.lower() == other.lastname.lower():
			if self.firstname.lower() < other.firstname.lower():
				return True
			elif self.firstname.lower() > other.firstname.lower():
				return False
			else:
				return "Same first and last names for %s and %s " %((self.firstname,
					self.lastname), (other.firstname, other.lastname))


"""
Creates four Employee objects and calls methods on them for testing purposes.
"""
if __name__ == "__main__":
	employee1 = Employee("Mickey", "Mouse", "597-938-9202", 60000)
	print(employee1)

	employee2 = Employee("Donald", "Duck", "597-938-0002", 70000)
	print(employee2)

	employee3 = Employee("Donald", "Duck", "980-797-9090", 87000)

	employee4 = Employee("Harrison", "Ford", "908-687-0010", 402000)

	employee1.giveRaise(10)
	print(employee1)

	employee2.giveRaise(15)
	print(employee2)

	print(employee2 == employee3)

	print(employee3 == employee1)

	print("\nComparison of two objects to check if object one is alphabetically less ")
	print(employee1 < employee2)
	
	print(employee4 < employee3)

	print(employee3 < employee2)

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

First object is  Donald Duck 
Second object is  Donald Duck
True
First object is  Donald Duck 
Second object is  Mickey Mouse
False

Comparison of two objects to check if object one is alphabetically less 
False
False
Same first and last names for ('Donald', 'Duck') and ('Donald', 'Duck') 

>>> 

'''

