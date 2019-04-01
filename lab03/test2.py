from random import shuffle
import sys

def histogram(tekst):
	iloscLiter = {}
	for i in range(0, len(tekst)):
		if(tekst[i]!=" "):	
			iloscLiter[tekst[i]] = tekst.count(tekst[i])
	return iloscLiter
	

def deck():
	global deck1
	deck1 = [("2","c"), ("2","d"), ("2","h"), ("2","s"),
			("3","c"), ("3","d"), ("3","h"), ("3","s"),
			("4","c"), ("4","d"), ("4","h"), ("4","s"),
			("5","c"), ("5","d"), ("5","h"), ("5","s"),
			("6","c"), ("6","d"), ("6","h"), ("6","s"),
			("7","c"), ("7","d"), ("7","h"), ("7","s"),
			("8","c"), ("8","d"), ("8","h"), ("8","s"),
			("9","c"), ("9","d"), ("9","h"), ("9","s"),
			("10","c"), ("10","d"), ("10","h"), ("10","s"),
			("J","c"), ("J","d"), ("J","h"), ("J","s"),
			("D","c"), ("D","d"), ("D","h"), ("D","s"),
			("K","c"), ("K","d"), ("K","h"), ("K","s"),
			("A","c"), ("A","d"), ("A","h"), ("A","s")]
	return deck1
	
def shuffle_deck():
	shuffle(deck1)
	return deck1

players=[0]*10
def deal(n):
	for i in range(0,n):
		print("Karty gracza ", (i+1))
		k1=deck1.pop()
		k2=deck1.pop()
		k3=deck1.pop()
		k4=deck1.pop()
		k5=deck1.pop()
		players[i]=k1,k2,k3,k4,k5
		print(players[i])

		print("")	
		
def hand_rank(n):											#n - numer gracza
	print("Statystyki gracza numer:", n)
	hand_rank_list = [item[0] for item in players[n-1]]		#wpisuje w liste same figury
	hand_color_list = [item[1] for item in players[n-1]]	#wpisuje w liste same kolory
	print(hand_rank_list)
	print(hand_color_list)
	
	hand_rank_histogram = histogram(hand_rank_list)			#wypisuje ile jest danych figur
	print(hand_rank_histogram)
	hand_color_histogram = histogram(hand_color_list)		#wypisuje ile jest danych kolorow
	print(hand_color_histogram)
	
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
