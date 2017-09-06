# CONNECT 4 Part: 2
#
# Building on part 1, implement the game loop for Connect 4 using the ConnectFour
# class. 
#
# The Connect 4 class should use the objects you created (Board and Piece) as building
# blocks. By the end of this exercise running the play method on a ConnectFour object
# should allow you fill the connect four board with pieces, and recognize when the 
# board is full.

from colorama import Fore, Back, Style

class Piece(object):
	def __init__(self, color):
		self.piece = '●'

	def __str__(self):
		return ''

class Board(object):
	def __init__(self):
		self.board = [
			['_']*7 for i in range(6)

		]
	
	def __str__(self):
		return ''

class ConnectFour(object):
	def __init__(self):
		self.Board = Board()
		self.players = ['red', 'yellow']

	def __str__(self):
		return 0

	def play(self):
		return 0

	def drop_piece(self):
		return 0

if __name__ == '__main__':
	game = ConnectFour()
	game.play()
