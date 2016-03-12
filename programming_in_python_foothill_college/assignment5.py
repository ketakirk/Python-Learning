""" Assignment #5 Submitted by Ketaki Kekatpure. Course - CS21A

"""
class Card:
	'''
	This class implements a card.

	'''
	def __init__(self, rank, suit):
		'''
		This function initializes the class and takes the rank and the 
		suit as the parameters.
		@type int 
		@param rank takes a rank between 1 and 13

		@type str 
		@param suit takes the first letter of the suit
		'''
		self._rank = rank
		self._suit = suit

	def getRank(self):
		'''
		This function returns a rank in the range of 1- 13 indicating the 
		ranks Ace through King.

		'''
		return self._rank

	def getSuit(self):
		'''
		This function returns the first letter of suit (diamonds, clubs, 
		hearts, spades) of the card.

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
		digit_to_text = {1: 'Ace', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 
						8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King', 
						's': 'Spades', 'd': 'Diamonds', 'c': 'Clubs', 'h': 'Hearts'}

		for k,v in digit_to_text.items():
			m = (digit_to_text[self._rank] + ' of ' + digit_to_text[self._suit])
		return m


if __name__ == '__main__':
	a = Card(11, 's')
	print(a.getRank())
	print(a.getSuit())
	print(a.bjValue())
	print(a)
	b = Card(4, 'd')
	print(b.getRank())
	print(b.getSuit())
	print(b.bjValue())
	print(b)
	c = Card(12, 'h')
	print(c)
	d = Card(5, 'c')
	print(d)
	e = Card(3, 'h')
	print(e)

'''---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------
OUTPUT

================================ RESTART ================================
>>> 
11
s
10
Jack of Spades
4
d
4
Four of Diamonds
Queen of Hearts
Five of Clubs
Three of Hearts
>>> 

'''