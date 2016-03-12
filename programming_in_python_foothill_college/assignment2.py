"""Assignment #2 submitted by Ketaki Kekatpure. Course - CS21A

This program prints three letters with different addressee, candidate 
and sender names for each letter. The names are hardcoded in the list-
'listOfinputs'."""


listOfinputs = [('Hildegard', 'Barbara Boxer', 'she', 'Brunhilda'), 
				('Cheech', 'Jerry Brown', 'he', 'Chong'),
				('Donald', 'Hillary Clinton', 'she', 'Jeb')]

letter = "Dear %s, \n\nI would like you to vote for %s \nbecause I think %s is best for this state.\n\nSincerely,\n%s \n\n"

for name in listOfinputs:
	print(letter % name)



"""
>>> ================================ RESTART ================================
>>> 
Dear Hildegard, 

I would like you to vote for Barbara Boxer 
because I think she is best for this state.

Sincerely,
Brunhilda 


Dear Cheech, 

I would like you to vote for Jerry Brown 
because I think he is best for this state.

Sincerely,
Chong 


Dear Donald, 

I would like you to vote for Hillary Clinton 
because I think she is best for this state.

Sincerely,
Jeb 


>>> 
"""


#-------------------------------------------------------------------------------------

"""
Challenge: This program takes the names of the addressee, candidate and sender as inputs
from the user. It stores the inputs in the list- listofNames. Once the user types 
'done' for the addressee, the program exits and prints the letters with different 
addressee, candidate and sender names.
"""

letter = "Dear %s, \n\nI would like you to vote for %s \nbecause I think she/he is best for this state.\n\nSincerely,\n%s \n\n"

listOfNames= []

while True:
    addressee = input("Please enter addressee name: ")
    if addressee == 'done':
        break
    candidate = input("Please enter candidate name: ")
    sender = input("Please enter sender name: ")
    
    
   
    listOfNames.append((addressee, candidate, sender))
    
for name in listOfNames:
    print(letter % name)


"""
================================ RESTART ================================
>>> 
Please enter addressee name: Jane
Please enter candidate name: John
Please enter sender name: Smith
Please enter addressee name: Harry
Please enter candidate name: Ron
Please enter sender name: Hagrid
Please enter addressee name: done
Dear Jane, 

I would like you to vote for John 
because I think she/he is best for this state.

Sincerely,
Smith 


Dear Harry, 

I would like you to vote for Ron 
because I think she/he is best for this state.

Sincerely,
Hagrid 


>>> 
"""
