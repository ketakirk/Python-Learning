""" Assignment #6 Submitted by Ketaki Kekatpure. Course - CS21A

"""

class Card:
	def __init__(self, rank, suit):
		'''
		This function initializes the class and takes the rank and the 
		suit as the parameters.
		@type int 
		@param rank takes a rank between 1 and 13

		@type str 
		@param suit takes the first letter of the suit
		'''

		suit_values = {'c', 'd', 'h', 's'}
		no_card = "No Card object has been created: "

		try:
			if not isinstance(rank, int) or rank != int(rank):
				raise TypeError(no_card + "This card's rank is not a number")
			elif rank < 1 or rank > 13:
				raise ValueError(no_card + "This card's rank is out of range")
			elif not isinstance(suit, str) or suit.isdigit():
				raise TypeError(no_card + "This card's suit is not a string")
			elif suit not in suit_values:
				raise ValueError(no_card + "This suit is not one of the strings in the set{'c', 'd', 'h', 's'}")			
			else:
				self._rank = rank
				self._suit = suit
		except NameError:
			raise NameError()

	def getRank(self):
		'''
		This function returns a rank in the range of 1- 13 indicating the 
		ranks Ace through King.

		'''
		return self._rank

	def getSuit(self):
		'''
		This function returns the suit (diamonds, clubs, hearts, spades) of 
		the card.

		'''
		return self._suit

	def bjValue(self):
		'''
		Returns the Blackjack value of a card. Ace counts as 1, face cards
		count as 10.
		'''
		return min(self._rank, 10)

	def __str__(self):
		'''
		Returns a string that names the card. For example: "Ace of Spades".
		'''
		digit_to_text = {1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 
						6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
						11: 'Jack', 12: 'Queen', 13: 'King', 
						's': 'Spades', 'd': 'Diamonds', 'c': 'Clubs', 'h': 'Hearts'}

		for k,v in digit_to_text.items():
			m = (digit_to_text[self._rank] + ' of ' + digit_to_text[self._suit])
		return m

def main():
	try:
		a = Card(13, '6')
	except TypeError as e:
		print(e)
		return
	except ValueError as e:
		print(e)
		return
	except NameError as e:
		print("No Card object has been created: This card's rank is not a number")
		return
	else:
		print(a)
		print("Rank = " , a.getRank())
		print("Suit = " , a.getSuit())
		print("Blackjack value = " , a.bjValue())


if __name__ == '__main__':
	main()




'''---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
INPUT
a = Card(1, 's')
a = Card(f, 'h')
a = Card(80, 'c')
a = Card(12, 'x')
a = Card(13, '6')

OUTPUT
Ace of Spades
Rank =  1
Suit =  s
Blackjack value =  1

No Card object has been created: This card's rank is not a number

No Card object has been created: This card's rank is out of range

No Card object has been created: This suit is not one of the strings in the set{'c', 'd', 'h', 's'}

No Card object has been created: This card's suit is not a string

'''