import collections
Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
	
	ranks = [ str(n) for n in range(2,11)] + list('JQKA')
	suites = 'spades hearts clubs diamonds'.split()
	def __init__(self):
		
		self._cards = [ Card(rank,suit) for suit in FrenchDeck.suites
										for rank in FrenchDeck.ranks]
	def __len__(self):
		return len(self._cards)
		
	def __getitem__(self,pos):
		return self._cards[pos]
		
	def __repr__(self):
		print 'FrenchDeck Cards len ' + len(self._cards)
		
beer_card = Card('7','diamonds')
print beer_card		

deck = FrenchDeck()
print len(deck)

index = 8
for i in range(0,4) :
	print deck[i]
	i += 13
from random import choice
print 'random shuffle'	

cardlist = [];
for i in range(10)	:
	cardlist.append(choice(deck))
	
	
if Card('5','spades') in deck:
		print 'contains'
		
if Card('5','spade') in deck:
		print 'spade contains'		
		
def card_high(card):
	
	rank = FrenchDeck.ranks.index(card.rank)
	suit_count = len(FrenchDeck.suites);
	type = suit_count - 1- FrenchDeck.suites.index(card.suit)
	return rank * suit_count + type;
	
for card in sorted(deck,key=card_high)	:
	print card;
	
			
