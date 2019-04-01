import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
	# Wait for a connection
	print('waiting for a connection')
	connection, client_address = sock.accept()
	try:
		print('connection from', client_address)

		# Receive the data in small chunks and retransmit it
		while True:
			data = connection.recv(64)
			print('received {!r}'.format(data))
			if data:
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

				print("Rozdane karty:")

				hands = deck.deal(players)
				print(players[0].cards_to_str() + " : " + str(get_player_hand_rank(players[0].get_player_hand_immutable())))
				print(players[1].cards_to_str() + " : " + str(get_player_hand_rank(players[1].get_player_hand_immutable())))
				print("Wyslane karty graczowi:")
				print(players[1].cards_to_str() + " : " + str(get_player_hand_rank(players[1].get_player_hand_immutable())))
				reka = bytes((players[1].cards_to_str() + " : " + str(get_player_hand_rank(players[1].get_player_hand_immutable()))), 'utf-8')
				
				connection.sendall(reka)
			else:
				print('no data from', client_address)
				break

	finally:
		# Clean up the connection
		connection.close()