#!/usr/bin/env python
# encoding: utf-8
import os
from colorama import Fore, Back, Style

clear = lambda: os.system('clear')

class Piece(object):
	"""
		Piece object, implements color display and equality comparators.
	"""
	def __init__(self, color):
		self.color = color
		if color == 'yellow':
			self.piece = Back.BLUE + Fore.YELLOW + Style.BRIGHT + '●' + Style.RESET_ALL
		else: 
			self.piece = Back.BLUE + Fore.RED + Style.BRIGHT + '●' + Style.RESET_ALL

	def get_color(self):
		return self.color

	def __str__(self):
		return self.piece

	def __eq__(self, other):
		if isinstance(self.__class__, other):
			if self.color == other.color:
				return True

		elif isinstance(other, str):
			if self.color == other:
				return True

		return False


class Board(object):
	def __init__(self):
		self.board = [
			['_']*7 for i in range(6)

		]
		self.bit_board = {
			'yellow': ['0'] * 48,
			'red': ['0'] * 48
		}

	def __str__(self):
		header = ' ' + ' '.join(['%d' % i for i in range(7)]) + ' \n'
		rows = ''
		for i in range(len(self.board)):
			rows += Back.BLUE + '|' + \
					(Back.BLUE + '|').join(map(lambda x: str(x),self.board[i])) \
					+ Back.BLUE + '|' + Style.RESET_ALL + '\n'

		return header + rows + Style.RESET_ALL
	
	def set_piece(self, piece, row, column):
		self.board[row][column] = piece
		self.bit_board[piece.get_color()][row + column*6 + column % 7] = '1'

	def get_board(self):
		return self.board

	def get_bit_board(self, piece):
		if isinstance(piece, str):
			board = self.bit_board[piece]
		else:
			board = self.bit_board[piece.get_color()]

		return ''.join(board)


class ConnectFour(object):
	def __init__(self):
		self.Board = Board()
		self.players = ['red', 'yellow']
		self.turn = 0

	def __str__(self):
		return str(self.Board)

	def play(self):
		winner = 0
		while (self.turn < 42) and (not winner):
			#clear()
			print self
			successful_placement= 0	
			while not successful_placement:
				column = int(raw_input("[%s's Turn] - Enter Column (0-6): " % self.players[self.turn %2]))
				message, successful_placement, new_piece = self.drop_piece(column)
				if message:
					print '\t' + message
				else:	
					winner = self.check_win(new_piece)
					if winner:
						winning_player = self.players[self.turn % 2]

			self.turn += 1

		#clear()
		print self
		if winner:
			print '\n%s wins!' % winning_player
		else:
			print "\nIt's a tie, better luck next time."

	def drop_piece(self, column):
		"""
			Inputs: 
				int column
			Returns: 
				tuple (str message, bool successful_placement)

			Description:
				Takes user column input and places a piece. Returns error message
				if column is invalid, or column is full.
		"""
		successful_placement = 0

		if column > 6:
			message = '*** Error *** Column out of range.\n'
			return (message, successful_placement, None)

		color = self.players[self.turn % 2]
		board_state = self.Board.get_board()
		row = 5
		for i in range(5,-1,-1):
			piece = board_state[i][column]
			if not isinstance(piece, Piece):
				successful_placement = 1
				new_piece = Piece(color)
				self.Board.set_piece(new_piece, row, column)		
				return (None, successful_placement, new_piece)

			row -= 1
	
		message = '*** Error *** Column full, try another.\n'
		return (message, successful_placement, None)

	def check_win(self, new_piece):
		"""
			Algorithm taken from: http://stackoverflow.com/q/7033165/1524592
			
			Intputs: 
				int row
				int	column
			Output:
				bool winner
		"""
		board = int(self.Board.get_bit_board(new_piece),2)
		print self.Board.get_bit_board('yellow')
		print self.Board.get_bit_board('red')


		y = board & (board >> 6)	
		if (y & (y >> 2*6)):
			return 1
		
		y = board & (board >> 7)
		if (y & (y >> 2*7)):
			return 1

		y = board & (board >> 8)
		if (y & (y >> 2*8)):
			return 1

		y = board & (board >> 1)
		if (y & (y >> 2)):
			return 1

		return 0
		

		
if __name__ == '__main__':
	game = ConnectFour()
	game.play()
