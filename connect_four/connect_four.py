#!/usr/bin/env python
# encoding: utf-8
import os
from colorama import Fore, Back, Style

clear = lambda: os.system('clear')

class Piece(object):
	def __init__(self, color):
		if color == 'yellow':
			self.piece = Back.BLUE + Fore.YELLOW + Style.BRIGHT + '●' + Style.RESET_ALL
		else: 
			self.piece = Back.BLUE + Fore.RED + Style.BRIGHT + '●' + Style.RESET_ALL

	def __str__(self):
		return self.piece

	def __eq__(self, other):
		if isinstance(self.__class__, other):
			if self.color == other.color:
				return True
		return False


class Board(object):
	def __init__(self):
		self.board = [
			['_']*7 for i in range(6)

		]
	
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

	def get_board(self):
		return self.board


class ConnectFour(object):
	def __init__(self):
		self.Board = Board()
		self.players = ['red', 'yellow']
		self.turn = 0

	def __str__(self):
		return str(self.Board)

	def play(self):
		while self.turn < 56:
			clear()
			print self
			column = int(raw_input("[%s's Turn] - Enter Column (0-6): " % self.players[self.turn %2]))
			self.drop_piece(column)
			
			self.turn += 1

	def drop_piece(self, column):
		color = self.players[self.turn % 2]

		board_state = self.Board.get_board()
		row = 5
		for i in range(5,-1,-1):
			piece = board_state[i][column]
			if not isinstance(piece, Piece):
				break
			row -= 1

		self.Board.set_piece(Piece(color), row, column)

		
if __name__ == '__main__':
	game = ConnectFour()
	game.play()
