""" Assignment #4 Submitted by Ketaki Kekatpure. Course - CS21A

This program takes whole number as a parameter and returns the number spelled out in text.
The input has to be less than positive and negative 1 billion."""


def getgroups(N):
	"""
	Expects a positive (>0) number and splits it into three groups and returns
	"""
	g1 = N % 1000
	N = N // 1000
	g2 = N % 1000
	N = N // 1000
	g3 = N

	return [str(g3), str(g2), str(g1)]
		
def num2word1(x):
	"""
	This function takes a single digit as an input and converts the number into text by
	by looking up in a dictionary
	"""
	units = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', \
				'6': 'six', '7': 'seven', '8': 'eight', '9':'nine'}
	if x == '0':
		return ''

	return units.get(x, "")

def num2word2(xy):
	"""
	This function takes two digits at the tens and units place as input and output text of the numbers.
	"""

	originals = {'01': 'one', '02': 'two', '03': 'three', '04': 'four', '05': 'five', '06': 'six', \
			'07': 'seven', '08': 'eight', '09':'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', \
			'13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', \
			'18': 'eighteen', '19': 'ninteen', '20': 'twenty', '30': 'thirty', '40': 'fourty', \
			'50': 'fifty', '60': 'sixty','70': 'seventy', '80': 'eighty', '90': 'ninety'}

	tens = {'2': 'twenty', '3': 'thirty', '4': 'fourty','5': 'fifty', '6': 'sixty',\
			'7': 'seventy', '8': 'eighty', '9': 'ninety'}


	if xy == '00':
		return ''

	if xy == int(xy):
		return ''

	if xy in originals:
		return originals[xy]
	else:
		tensp = xy[0]
		unitsp = xy[1]
		return tens[tensp] + ' ' + num2word1(unitsp)

def num2word3(xyz, suffix = ''):
	"""
	This function takes three numbers and the suffix(million, thousand) as input converts the
	numbers into text.	
	"""
	
	s = len(xyz)
	if s == 1 and xyz == '0':
		return ''

	if s == 1:
		xyz = '00' + xyz
	
	if s == 2:
		xyz = '0' + xyz

	if s > 3:
		print("invalid number")
		return ''

	hundp = xyz[0]
	unitensp = xyz[1:]

	if unitensp == '00':
		return num2word1(hundp) + ' hundred ' + ' ' + suffix
	elif hundp == '0':
		return num2word2(unitensp) + ' ' + suffix
	else:
		return num2word1(hundp) + ' hundred and ' + num2word2(unitensp) + ' ' + suffix

def validate(numstr):
	"""
	Validates a string of digits and returns a converted integer value. 
	If the string cannot be converted into an integer, an exception is thrown
	"""
	# If the number cannot be converted into an integer, _something_ is wrong. 
	# return 'invalid'
	try:
		N = int(numstr)
	except ValueError:
		raise ValueError

	# If the number is too large, rerutn invalid
	if len(str(numstr)) > 9:
		raise ValueError

	return N

def totext(num):
	"""
	Converts an arbitrary number (upto 9 digits) to words
	Example: totest(9001) === Nine thousand one
	"""

	# Run 'validate' in 'safe' mode
	try:
		N = validate(num)
	except ValueError:
		return "invalid"

	# At this point, N is established as a valid number with less than 9 digit. 

	# If 0, print 'zero' and return
	if N == 0:
		return "zero"

	# Check for negative and populate 'prefix'
	if N < 0:
		prefix = "minus"
	else:
		prefix = ""

	# Number is eligible and safe to be processed further.
	g = getgroups(abs(N))
	text = num2word3(g[0], 'million ') + num2word3(g[1] , 'thousand ') + num2word3(g[2])
	return "%s %s" %(prefix, text)

def tests():
	tocheck = ["b", 0, 1, -1, 1001, 987654321, -123456789, 900000001,
				"a", 10001]

	for num in tocheck:
		print("num = %s\nwords = %s\n\n" %(num, totext(num)))

def main():
	"""
	This function gets user input and calls totest() to convert into words.
	"""
	num = input("Please enter a number: ")
	print(totext(num))


if __name__ == '__main__':
	#main()
	tests()

'''---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
OUTPUT

================================ RESTART ================================
>>> 
num = b
words = invalid


num = 0
words = zero


num = 1
words =  one 


num = -1
words = minus one 


num = 1001
words =  one thousand one 


num = 987654321
words =  nine hundred and eighty seven million six hundred and fifty four thousand three hundred and twenty one 


num = -123456789
words = invalid


num = 900000001
words =  nine hundred  million one 


num = a
words = invalid


num = 10001
words =  ten thousand one 


>>> 
'''






