# 5.2 Write a program that repeatedly prompts a user for integer 
# numbers until the user enters 'done'. Once 'done' is entered, 
# print out the largest and smallest of the numbers. If the user 
# enters anything other than a valid number catch it with a try/except 
# and put out an appropriate message and ignore the number. Enter the 
# numbers from the book for problem 5.1 and Match the desired output as shown.

largest = None
smallest = None
while True:
	num = input("Enter a number: ")
	if num == 'done' : break
	# print(num)

	# Catch if it is not a valid number

	try:
		num = int(num)
	except:
		print("Invalid input")
		continue

	# Find maximum number
	if largest is None:
		largest = num
	elif num > largest:
		largest = num
	
	print("Maximum is", largest)

	# Find minimum number
	if smallest is None:
		smallest = num
	elif num < smallest:
		smallest = num

	print("Minimum is", smallest)
