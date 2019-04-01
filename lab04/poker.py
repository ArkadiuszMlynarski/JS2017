from random import shuffle
import sys


class Card:
	# słownik symboli unicode
	unicode_dict = {'s': '\u2660', 'h': '\u2665', 'd': '\u2666', 'c': '\u2663'}
	   
	def __init__(self, rank, suit):
	# TODO: definicja metody
		self.__rank_ = rank
		self.__suit_ = suit
		
	def get_value(self):
	# TODO: definicja metody (ma zwracać kartę w takiej reprezentacji, jak dotychczas, tzn. krotka)
		return [self.__rank_, self.__suit_]
		
	def __str__(self):
	# TODO: definicja metody, przydatne do wypisywania karty	
		return str(self.__rank_) + str(self.__suit_)

		
	def show(self):
		if self.__rank_ == 14:
			rank = "A"
		elif self.__rank_ == 11:
			rank = "J"
		elif self.__rank_ == 12:
			rank = "Q"
		elif self.__rank_ == 13:
			rank = "K"
		else:
			rank = self.__rank_

		return "{}{}".format(rank, self.__suit_)
		
class Deck():
	
	def __init__(self, *args):
	# TODO: definicja metody, ma tworzyć niepotasowaną talię (jak na poprzednich lab)
		self.__deck_ = []
		self.build()
		self.__players_ = []
		
	def build(self):
		for suit in ["\u2660", "\u2663", "\u2666", "\u2665"]:
			for rank in range(2, 15):
				self.__deck_.append(Card(rank, suit))
				
	def show(self):
		for card in self.__deck_:
			print (card.show(), end=" ")
			
	def __str__(self):
	# TODO: definicja metody, przydatne do wypisywania karty
		return str(self.__deck_)
		
	def shuffle(self):
	# TODO: definicja metody, tasowanie
		shuffle(self.__deck_)
		
	def deal(self, players):
	# TODO: definicja metody, otrzymuje listę graczy i rozdaje im karty wywołując na nich metodę take_card z Player
		for i in players:	
			for l in range(0,5): 
				i.take_card(self.__deck_.pop())	

class Player():

	def __init__(self, money, name=""):
		self.__stack_ = money
		self.__name_ = name
		self.__hand_ = []

	def take_card(self, card):
		self.__hand_.append(card.show())
			
	def get_stack_amount(self):
		return self.__stack_
		
	def get_player_hand_immutable(self):
		return tuple(self.__hand_)

	def cards_to_str(self):
	# TODO: definicja metody, zwraca stringa z kartami gracza
		# for c in self.__hand_:
			# print (c.show(), end=" ")
		return str(self.__hand_)


def histogram(tekst):
	iloscLiter = {}
	for i in range(0, len(tekst)):
		if(tekst[i]!=" "):	
			iloscLiter[tekst[i]] = tekst.count(tekst[i])
	return iloscLiter

# slownik wartosci kart w postaci int, dwojka - 2, ...., as - 14
card_rank_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
					"8": 8, "9": 9, "10": 10, "J": 11, "D": 12,
					"K": 13, "A": 14}


def get_player_hand_rank(hand):
	hand_rank_list = []  
	hand_color_list = []
	
	for i in hand:
		hand_rank_list.append(i[0])	
		hand_color_list.append(i[1])
	
	hand_rank_histogram = histogram(hand_rank_list)			#wypisuje ile jest danych figur
	hand_color_histogram = histogram(hand_color_list)		#wypisuje ile jest danych kolorow
	
	def is_rank_sequence():
		if(hand_rank_list[0]=='A' and hand_rank_list[1]=='K' and hand_rank_list[2]=='Q' and hand_rank_list[3]=='J' and hand_rank_list[4]=='10'):
			return True
		if(hand_rank_list[0]=='K' and hand_rank_list[1]=='Q' and hand_rank_list[2]=='J' and hand_rank_list[3]=='10' and hand_rank_list[4]=='9'):
			return True
		if(hand_rank_list[0]=='Q' and hand_rank_list[1]=='J' and hand_rank_list[2]=='10' and hand_rank_list[3]=='9' and hand_rank_list[4]=='8'):
			return True
		if(hand_rank_list[0]=='J' and hand_rank_list[1]=='10' and hand_rank_list[2]=='9' and hand_rank_list[3]=='8' and hand_rank_list[4]=='7'):
			return True
		if(hand_rank_list[0]=='10' and hand_rank_list[1]=='9' and hand_rank_list[2]=='8' and hand_rank_list[3]=='7' and hand_rank_list[4]=='6'):
			return True	
		if(hand_rank_list[0]=='9' and hand_rank_list[1]=='8' and hand_rank_list[2]=='7' and hand_rank_list[3]=='6' and hand_rank_list[4]=='5'):
			return True
		if(hand_rank_list[0]=='8' and hand_rank_list[1]=='7' and hand_rank_list[2]=='6' and hand_rank_list[3]=='5' and hand_rank_list[4]=='4'):
			return True
		if(hand_rank_list[0]=='7' and hand_rank_list[1]=='6' and hand_rank_list[2]=='5' and hand_rank_list[3]=='4' and hand_rank_list[4]=='3'):
			return True
		if(hand_rank_list[0]=='6' and hand_rank_list[1]=='5' and hand_rank_list[2]=='4' and hand_rank_list[3]=='3' and hand_rank_list[4]=='2'):
			return True
		else:
			return False
	is_hand_rank_sequence = is_rank_sequence() 
	
	hand_strength=0
	if( (5 in hand_color_histogram.values()) and ( 'A' in hand_rank_list ) and is_hand_rank_sequence):
		hand_strength = (10, "Krolewski poker")
	elif((5 in hand_color_histogram.values()) and is_hand_rank_sequence):
		hand_strength = (9, "Poker")	
	elif(4 in hand_rank_histogram.values()):
		hand_strength = (8, "Kareta")
	elif(3 in hand_rank_histogram.values() and 2 in hand_rank_histogram.values()):
		hand_strength = (7, "Full")
	elif(5 in hand_color_histogram.values()):
		hand_strength = (6, "Kolor")
	elif(is_hand_rank_sequence):
		hand_strength = (5, "Strit")
	elif(3 in hand_rank_histogram.values()):
		hand_strength = (4, "Trojka")
	elif(2 in hand_rank_histogram.values() and len(hand_rank_histogram)==3):
		hand_strength = (3, "Dwie pary")
	elif(2 in hand_rank_histogram.values()):
		hand_strength = (2, "Para")
	
	return hand_strength
