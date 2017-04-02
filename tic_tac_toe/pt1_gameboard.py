# TIC-TAC-TOE Part 1:
# 
# The goal of this exercise is create a small program that will print out a tic-tac-toe
# game board.
#
# This exercise will test your knowledge of lists and conditional statements.



# One of the main things you need to do when programming a game of tic-tac-toe
# is showing the players the game board.
#
# Write a program that prints the game_board matrix and like:
#
#  0 | 1 | 2
# --- --- ---
#  3 | 4 | 5
# --- --- ---
#  6 | 7 | 8
#
# Where if the the game board has a piece placed print the piece, otherwise print
# the cell.

def print_board(game_board):
	return 0

# This is the primary game loop, you will run the tic-tac-toe game using this
def tic_tac_toe():

	# You can think of the "game board" in tic-tac-toe like a list, where each 
	# item in the list is another list.
	# 
	# This "game_board" is essentially a 3x3 matrix, that will represent the tic-tac-toe
	# game.

	game_board = [
		[None, None, None],
		[None, None, None],
		[None, None, None]
	]

	print_board(game_board)

