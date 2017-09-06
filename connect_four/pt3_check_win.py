# CONNECT 4 Part: 3
#
# Write the check win method for connect four. As long as it works it's okay! Don't  
# worry about its efficiency for now.
#
# Once you're done feel free to look online for some other interesting ways to solve
# this problem.

import os
from colorama import Fore, Back, Style

clear = lambda: os.system('clear')

class Piece(object):
	def __init__(self, color):
		self.piece = '●'

	def __str__(self):
		return ''
	
	def get_color(self):
		return 0
	
	def __eq__(self, other):
		return False


class Board(object):
	def __init__(self):
		self.board = [
			['_']*7 for i in range(6)

		]
	
	def __str__(self):
		return ''

	def set_piece(self):
		return 0

	def get_board(self):
		return 0
	
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

	def check_win(self):
		return 0

if __name__ == '__main__':
	game = ConnectFour()
	game.play()
