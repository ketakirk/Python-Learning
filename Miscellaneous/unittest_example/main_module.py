from datetime import datetime

def seconds_to_isotimestamp(scnds):
	"""
	Converts 'scnds' (seconds since epoch (Jan 1 1970)) to a data string
	"""
	dtobj = datetime.fromtimestamp(scnds)
	fmt = "%Y-%m-%d %H:%M:%S"
	return dtobj.strftime(fmt)	



def remove_vowels(strng):
	"""
	Removes vowels (aeiouAEIOU) from 'strng'
	"""
	vwls = "aeiouAEIOU"
	retstring = strng
	for v in vwls:
		retstring = retstring.replace(v, "")

	return retstring

def remove_odds(numlist):
	"""
	Returns even numbers from 'numlist'
	"""
	return [num for num in numlist if num % 2 == 0]