# 8.4 Open the file romeo.txt and read it line by line. For each line, 
# split the line into a list of words using the split() method. The 
# program should build a list of words. For each word on each line 
# check to see if the word is already in the list and if not append 
# it to the list. When the program completes, sort and print the resulting 
# words in alphabetical order.
# You can download the sample data at http://www.pythonlearn.com/code/romeo.txt


fhand = open('romeo.txt')
# first aggregate all words
complete = []
for line in fhand:
	complete.extend(line.split())

	# Method 2: with +
	# complete = complete + line.split()

# create a new list with lowercased words from "complete"
text = []
for word in complete:
	text.append(word.lower())
#print(complete)
text.sort()
print("All words = %s" % text)

# delete repeated words from text, using basic algoritm
print("\n===== Basic algorithm =====\n")
unique = []
for idx in range(len(text)- 1):
	current = text[idx]
	next = text[idx + 1]
	if current != next:
		unique.append(current)
unique.append(text[-1])
print(unique)

# Create a set of unique words
print("\n===== Using Set =====\n")
unique2 = set(text)
sorted_uniques = sorted(unique2)
print ("sorted unique names  = %s" % sorted_uniques)
