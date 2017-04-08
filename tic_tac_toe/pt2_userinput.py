# TIC-TAC-TOE Part 2:
# 
# After finishing part 1, you should have a function that draws the game board.
# The goal for part 2 is to give users the ability to place their pieces 'x' or 'o'
# in the positions (0-8) on the game baord
#
# The insert_move() funciton should take a user input and replace the game board 
# with a tic-tac-toe piece: 
#
#  0 | 1 | 2      0 | 1 | 2
# --- --- ---    --- --- ---
#  3 | 4 | 5  =>  3 | x | 5  
# --- --- ---    --- --- ---
#  6 | 7 | 8      6 | 7 | 8
#
# You can use raw_input() function to get the user's input.  
#
def insert_move():
	return 0

def print_board(game_board):
	#
	# Your working code goes here
	#
	return 0



# This is the primary game function, you will run the tic-tac-toe game using this
def tic_tac_toe():

	game_board = [
		[None, None, None],
		[None, None, None],
		[None, None, None]
	]

	print_board(game_board)
	
	#
	# Call insert_move() here and the print the gameboard again 
	# to test and make sure the the move was saved properly
	#

	print_board(game_board)
