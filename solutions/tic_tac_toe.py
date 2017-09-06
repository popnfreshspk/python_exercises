#!/usr/bin/env python
import os

clear = lambda: os.system('clear')

def print_board(board):
	print ""
	counter = 0
	for row in board:
		current_row = " %s | %s | %s" % (tuple([row[i] if row[i] else str(counter*3 + i) for i in range(3)]))
		print current_row
		if counter < 2:
			print "--- --- ---"
		counter +=1

def insert_move(input_position, moves, game_board):
	row_value = input_position/3
	column_value = input_position % 3

	if game_board[row_value][column_value] is None:
		game_board[row_value][column_value] = 'x' if moves % 2 == 0 else 'o'
		return 0
	else:
		print ""
		print "******************************"
		print "* ERROR: %s is there already *" % game_board[row_value][column_value]
		print "******************************"
		print ""
		return 1, 

def check_win(board, moves, input_position):
	turn = 'x' if moves % 2 == 0 else 'o'
	corners = [0,2,6,8]
	win = 0

	row = input_position/3
	col = input_position % 3

	if check_row_win(board,turn,row) or check_column_win(board,turn,col):
		return 1

	if input_position in corners:
		return check_corner_win(board,turn,row,col)

	return 0

def check_row_win(board,turn,row):
	if board[row][0] == board[row][1] == board[row][2] == turn:
		board[row][0] = board[row][1] = board[row][2] = turn.upper()
		return 1
	else:
		return 0


def check_column_win(board,turn, col):
	if board[0][col] == board[1][col] == board[2][col] == turn:
		board[0][col] = board[1][col] = board[2][col] = turn.upper()
		return 1
	else:
		return 0

def check_corner_win(board,turn,row,col):
	if row == col:
		if board[0][0] == board[1][1] == board[2][2] == turn:
			board[0][0] = board[1][1] = board[2][2] = turn.upper()
			return 1
	else:
		if board[0][2] == board[1][1] == board[2][0] == turn:
			board[0][2] = board[1][1] = board[2][0] = turn.upper()
			return 1
	return 0


def tic_tac_toe():
	game_board = [
		[None]*3 for i in range(3)
	]
	
	moves = 0
	win = 0 
	while moves < 9 and not win:
		clear()
		print "Current Game Board:"
		print_board(game_board)
		print ""

		# short loop to check for valid piece placement
		invalid_move = 1
		while invalid_move and not win:
			input_position = int(raw_input("[%s's Turn] - Enter move (0-8): " % ('x' if moves % 2 == 0 else 'o')))
			invalid_move = insert_move(input_position, moves, game_board)
			if invalid_move:
				print_board(game_board)

		win = check_win(game_board, moves, input_position)
		if win:
			clear()
			print_board(game_board)
			print ""
			print ('x' if moves % 2 == 0 else 'o') + ' Wins!'
		moves += 1

	if not win:
		print "It's a tie!"

if __name__ == '__main__':
	tic_tac_toe()
