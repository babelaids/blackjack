import random


values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace': 11}
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
		new_card = self.deck.pop()
		return new_card

class Hand():

	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,new_card):
		
		self.cards.append(new_card)
		self.value += values[new_card.rank]
		if new_card.rank == "Ace":
			self.aces += 1

	def ace_high(self):
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1

class Chips():
	def __init__(self):
		self.buy_in = 100
		self.bet = 0
	
	def add_bet(self,amount):
		self.bet += amount

	def win_bet(self):
		self.buy_in += self.bet*2

	def lost_bet(self):
		self.buy_in -= self.bet


def take_bet(chips):
	while True:
		try:	
			chips.bet = int(input(f"How much would you like to bet? Your total is {chips.buy_in}"))
		except:
			print('Use a number please.')
		if chips.buy_in >= chips.bet:
			chips.buy_in -= chips.bet
			return (f" you bet {chips.bet}. You have {chips.buy_in} left.")
			break
			
		else:
			print("You can't afford that!")

def hit(deck,hand):
	single_card = deck.deal()
	hand.add_card(single_card)

def hit_stand(deck,hand):
	global playing
	while True:
		
		x = input("Will you Hit or Stand? (type h or s).  ")
		
		if x.lower() == "h":
			hit(deck,hand)
		elif x.lower() == "s":
			print(f" You have {hand.value}. Dealer's turn!")
			playing = False
		else:
			print("please enter H or S only.")
			continue
		break

def show_some(player,dealer):
	print("Dealer's hand:  ")
	print("(first card hidden)")
	print(dealer.cards[1])

	print("Player's hand:")
	for card in player.cards:
		print(card)
	print(f"({player.value})")


def show_all(player,dealer):

	print("/n Dealer's hand:")
	for card in dealer.cards:
		print(card)
	print(f"({dealer.value})")

	print("/n Player's hand:")
	for card in player.cards:
		print(card)
	print(f"({player.value})")

def player_busts(player,dealer,chips):
	print("Player BUSTS!")
	chips.lost_bet()

def player_wins(player,dealer,chips):
	print("PLAYER WINS!")
	chips.win_bet()

def dealer_busts(player,dealer,chips):
	print("Dealer BUSTS! PLAYER WINS!")
	chips.win_bet()

def dealer_wins(player,dealer,chips):
	print("Dealer WINS!")
	chips.lost_bet()

def push(player,dealer):
	print("It's a tie! PUSH")

