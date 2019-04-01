from poker import *

num_players = 2
players = []

for i in range (0, num_players):
    players.append(Player(1000))

print("Nowa talia:")
deck = Deck()
deck.show()
print()

print("Talia potasowana:")
deck.shuffle()
deck.show()
print()

print("Rozdane karty 2 graczom:")

hands = deck.deal(players)
for player in players:
	print(player.cards_to_str() + " : " + str(get_player_hand_rank(player.get_player_hand_immutable())))
