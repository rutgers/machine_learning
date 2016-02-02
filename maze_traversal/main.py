import environment as env
import pprint
import random
import sys
import algo
import datetime
import csv
from cell import Cell
# import pdb



def create_mazes():
	''' This function should generate 10 grids, as a list of lists, with size 100x100.
		You can use existing code or write your own for this.
	'''

def get_start_and_goal(grid):
	'''
	Use this function to decide where the Agent will start and what its goal is
	'''




if __name__ == '__main__':

	# Get rid of the .pyc files that get generated on each run
	sys.dont_write_bytecode = True 
	pp = pprint.PrettyPrinter()

	if len(sys.argv) != 3:
		print "Format: python main.py <path to maze file> <tiebreak val: 1 for smaller g, 0 for larger g>"
		sys.exit(1)
	else:
		maze_file = sys.argv[1]

	# for i in range(1,11):
	# 	grid = env.generate_grid(10)
	# 	env.write_csv(grid,'mazes/small_mazes/small_maze_{0}.csv'.format(i))

	grid, size = env.read_grid('mazes/small_mazes/small_maze_2.csv')

	algo.print_grid(grid)
	# start = Cell(0,0,101)
	# goal = Cell(100,100,101)

	''' 
	Use this space to begin manipulating the agent, reading in the maze from the csv file,
	and making calls to search functions
	'''