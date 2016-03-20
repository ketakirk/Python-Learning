# 9.4 Write a program to read through the mbox-short.txt and figure 
# out who has the sent the greatest number of mail messages. The 
# program looks for 'From ' lines and takes the second word of those 
# lines as the person who sent the mail. The program creates a Python 
# dictionary that maps the sender's mail address to a count of the number 
# of times they appear in the file. After the dictionary is produced, 
# the program reads through the dictionary using a maximum loop to find 
# the most prolific committer.

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emails = dict()
for line in handle:
    words = line.split()
    if len(words) == 0 : continue
    if words[0] != ('From') : continue
    mail = words[1]
    emails[mail]= emails.get(mail,0)+ 1
count = None
email = None
for keys, values in emails.items():
    if count is None or values > count:
        email = keys
        count = values
print email, count