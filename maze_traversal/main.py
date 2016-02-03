import environment as env
import pprint
import sys
import algo
from cell import Cell
# import pdb

if __name__ == '__main__':

	# Get rid of the .pyc files that get generated on each run
	sys.dont_write_bytecode = True
	pp = pprint.PrettyPrinter()

	if len(sys.argv) != 2:
		print "Format: python main.py <path to maze file>"
		sys.exit(1)
	else:
		maze_file = sys.argv[1]

	grid, size = env.read_grid(maze_file)

	
	start = Cell(0,0,101)
	goal = Cell(9,9,101)

	algo.print_grid(grid, start, goal)

	algo.a_star(start, goal, grid)
