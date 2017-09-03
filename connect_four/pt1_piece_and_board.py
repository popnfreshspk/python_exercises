# CONNECT 4 Part: 1
#
# This exercise should expand on the TIC-TAC-TOE learning and let you explor
# implementing programs with classes.
#
# The output of your game board should look like the following:
#
#  0 1 2 3 4 5 6
# |_|_|_|_|_|_|_|
# |_|_|_|_|_|_|_|
# |_|_|_|_|_|_|_|
# |_|_|_|_|_|_|_|
# |_|_|_|_|_|_|_|
# |●|_|_|●|_|_|_|
#
# The challenge here is that you will need to color the pieces to indicate to the 
# players which piece has been dropped.
#
# You can use the colorama library to do this: https://pypi.python.org/pypi/colorama


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


