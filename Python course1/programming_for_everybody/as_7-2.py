# 7.2 Write a program that prompts for a file name, then opens that 
# file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of 
# the lines and compute the average of those values and produce an 
# output as shown below. Do not use the sum() function or a variable 
# named sum in your solution.
# You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt 
# when you are testing below enter mbox-short.txt as the file name.


fname = input('Enter a filename: ')

try:
	fh = open(fname)
except:
	print('File cannot be opened')

def get_num(s):
	return float(s.split(":")[1])

# main
total = 0
count = 0
average = 0

# fh = open("mbox-short.txt")
for line in fh:
	if line.startswith('X-DSPAM-Confidence:'):
		# print(get_num(line))
		total = total + get_num(line)
		count = count + 1
average = total/count
print(average)

