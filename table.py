import random


values = {'Ace':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'HighAce': 11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

class Card():
	def __init__(self,suit,rank):
		
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return self.rank+" of "+ self.suit

class Deck():

	def __init__(self):
		
		self.deck =[]

		for suit in suits:
			for rank in ranks:
				
				created_card = Card(suit,rank)
				self.deck.append(created_card)

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		return self.deck.pop()

class Hand():

	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = []

	def add_card(self,new_card):
		if type(new_card) == type([]):
			self.cards.extend(new_card)
		else:
			self.cards.append(new_card)

	def got_ace(self):
		if Deck.deal == values["Ace"]:
			if type(self.aces) == type([]):
				self.aces.append('x')

	def ace_high(self):
		for ace in self.aces():
			if self.value + 10 < 21:
				self.value["Ace"] = self.value["HighAce"]
			else:
				pass

class Chips():
	def __init__(self):
		self.buy_in = 0
		self.bet = 0
	
	def add_bet(self,amount):
		self.bet += amount

	def win_bet(self):
		self.buy_in += self.bet

	def lost_bet(self):
		self.buy_in -= self.bet


#def take_bet():
	#while True:
		#try:	
			#Chips.bet += int(input(f"How much would you like to bet? Your total is {Chips.buy_in}"))
		#except:
			#print('Use a number please.')
		#if Chips.buy_in >= Chips.bet:
		#	Chips.buy_in -= Chips.bet
			
		#else:
			#print("You can't afford that!")


pass