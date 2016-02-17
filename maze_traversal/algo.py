from binary_heap import BHeap
import math
import pprint
pp = pprint.PrettyPrinter()

from agent import Agent
from cell import Cell

infinity = 1000000

fringe = BHeap()
costs = {}

def print_grid(grid, agent, goal):
	'''
	Use the function to print the world state to the terminal.
	agent is your Agent, goal is the goal Cell.
	'''
	matrix = [['x' for i in range(len(grid[0]))] for j in range(len(grid[1]))]
	for i in range(10):
		for j in range(10):
			if i == agent.x and j == agent.y:
				matrix[i][j] = 'A'
			elif i == goal.x and j == goal.y:
				matrix[i][j] = 'G'
			elif grid[i][j].status == 'u':
				matrix[i][j] = ' '
			else:
				matrix[i][j] = 'X'

	pp.pprint(matrix)

def heuristic(a,b):
	'''
	Define your heuristic from Cell a to Cell b here.
	You can choose the Manhattan Distance as a starting point.
	Return a number.
	'''

def get_neighbors(cell,grid):
	'''
	Return a list of all unblocked neighbors of given cell.
	Check all four directions, as long as it's on the grid.
	Use the isBlocked() to check if a cell is blocked.
	'''
	neighbors = []

	return neighbors

def a_star(position,goal,grid):
	''' Implement A* here '''
	for count in range(500):
		# TODO add moves to fringe and/or update costs

		# TODO choose best move

		# TODO make move (update position)

		if fringe.size() == 0:
			print 'Maze is impossible. :('
			return

		print_grid(grid, position, goal)

		if position.x == goal.x and position.y == goal.y:
			print 'I did it!'
			return
