import environment as env
import pprint
import random
import sys
import algo
import datetime
import csv
from cell import Cell
# import pdb

if __name__ == '__main__':

	# Get rid of the .pyc files that get generated on each run
	sys.dont_write_bytecode = True 
	pp = pprint.PrettyPrinter()

	if len(sys.argv) != 3:
		print "Format: python main.py <path to maze file>"
		sys.exit(1)
	else:
		maze_file = sys.argv[1]


	grid, size = env.read_grid(maze_file)

	algo.print_grid(grid)
	start = Cell(0,0,101)
	goal = Cell(100,100,101)

	''' 
	Use this space to begin manipulating the agent, reading in the maze from the csv file,
	and making calls to search functions
	'''