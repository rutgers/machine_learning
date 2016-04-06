import pprint
import os
import board

if __name__ == '__main__':
	print "Welcome to Tic-Tac-Toe!\nWe\'ll fill in more description about usage here"

	won = False
	won_by_user = False
	won_by_ai = False
	stalemate = False

	config = [['u' for j in range(3)] for i in range(3)]
	test = board.Board(config)

	while not won or not stalemate:
		print "This is the current state of the board:\n"
	
		test.display()

		inputs = raw_input("Enter the coordinates of your move as a comma-separated list (ex.: x,y): ")

		'''
			Write the logic for handling errors in the input here. Consider errors like:
				- More than 2 arguments
				- Less than 2 arguments
				- Coordinates defined outside the space of the board
				- Coordinates that are not integers
		'''

		input_list = inputs.split(',')
		inputs = [int(x.strip()) for x in input_list]
		x = inputs[0]
		y = inputs[1]

		if test.set_value(int(x),int(y),'x') == False:
			print "wowowewa"
			continue

		# AI makes move here. We will write this using our knowledge of adversarial search.

		result = test.win()
		if result == 1:
			won = True
			won_by_user = True
			stalemate = True
		elif result == 2:
			won = True
			won_by_ai = True
			stalemate = True
		elif test.stalemate():
			stalemate = True

	if won_by_user:
		print "Congratulations! You win!"
	elif won_by_ai:
		print "Sorry. The AI won this round"
	elif stalemate:
		print "You played the AI to a stalemate"
