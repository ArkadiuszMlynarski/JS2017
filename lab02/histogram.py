from random import shuffle

def histogram(tekst):
	iloscLiter = {}
	for i in range(0, len(tekst)):
		if(tekst[i]!=" "):	
			iloscLiter[tekst[i]] = tekst.count(tekst[i])
	print(iloscLiter)
	

def deck():
	global deck
	deck = [("2","c"), ("2","d"), ("2","h"), ("2","s"),
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
	print(deck)
	
def shuffle_deck():
	shuffle(deck)
	print(deck)

def deal(n):
	for i in range(0,n):
		print("Karty gracza ", (i+1))
		for x in range(0,5):
			print(deck.pop(), end=" ")
		print("")	