import csv
import pprint
import random
import sys
from cell import Cell
import pdb

###########################
# DO NOT MODIFY THIS FILE #
###########################





'''
From Wikipedia:
Make the initial cell the current cell and mark it as visited
While there are unvisited cells
	If the current cell has any neighbours which have not been visited
		Choose randomly one of the unvisited neighbours
		Push the current cell to the stack
		Remove the wall between the current cell and the chosen cell
		Make the chosen cell the current cell and mark it as visited
	Else if stack is not empty
		Pop a cell from the stack
		Make it the current cell
'''

# Algorithm described in project description to set blocked statuses

def determine_blocked_status():
	number = random.randrange(0,sys.maxint) % 10
	if number <= 2:
		return "b"
	elif number > 2:
		return "u"

# Returns list of unvisited neighbors. Cells are tuples of coordinates
def find_unvisited_neighbors(cell,size,visited):
	i = cell[0]
	j = cell[1]

	# Get initial neighbors list
	if i == 0 and j == 0:
		neighbors = [(i+1,j),(i,j+1)]
	elif i == 0 and j == size-1:
		neighbors = [(i,j-1),(i+1,j)]
	elif i == size-1 and j == size-1:
		neighbors = [(i-1,j),(i,j-1)]
	elif i == size-1 and j == 0:
		neighbors = [(i-1,j),(i,j+1)]
	elif i == 0:
		neighbors = [(i,j-1),(i,j+1),(i+1,j)]
	elif i == size-1:
		neighbors = [(i,j-1),(i,j+1),(i-1,j)]
	elif j == 0:
		neighbors = [(i-1,j),(i+1,j),(i,j+1)]
	elif j == size-1:
		neighbors = [(i-1,j),(i+1,j),(i,j-1)]
	else:
		neighbors = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]

	# pdb.set_trace()
	# Items to remove from neighbors
	r = list()

	for item in neighbors:
		if item in visited:
			r.append(item)

	for item in r:
		neighbors.remove(item)

	# pdb.set_trace()
	return neighbors

# Write grid to output file
def write_csv(grid,output_file):
	f = open(output_file,'w')
	writer = csv.writer(f)

	size = len(grid)

	# First line is the size of the matrix
	# x means to ignore the value
	writer.writerow((size,size,'x'))

	for i in range(0,size):
		for j in range(0,size):
			writer.writerow((i,j,grid[i][j]))

	f.close()

# Read grid from input file. Returns fully populated grid
def read_grid(input_file):
	f = open(input_file,'r')

	reader = csv.reader(f)

	# pdb.set_trace()
	for row in reader:
		if row[2] == 'x':
			size = int(row[0])
			grid = [['x' for i in range(size)] for j in range(size)]
		else:
			i = int(row[0])
			j = int(row[1])	
			grid[i][j] = row[2]

	converted_grid = tuples_to_objects(grid)
	return converted_grid, size

# Use recursive back-tracking to generate grid
def generate_grid(size):

	# Create initial grid
	grid = [["x" for i in range(size)] for j in range(size)]

	# Initialize algorithm
	visited = list()	
	unvisited = list() # Maybe make this a BST? For efficiency's sake
	stack = list() # append() adds to the end of the list, pop() without arguments removes last element in the list

	# Select random cell in grid to start at
	current_cell = (random.randrange(0,sys.maxint) % size, random.randrange(0,sys.maxint) % size)
	visited.append(current_cell)

	grid[current_cell[0]][current_cell[1]] = 'u'

	# Make all other cells unvisited
	for i in range(size):
		for j in range(size):
			cell = (i,j)
			if cell != current_cell:
				unvisited.append(cell)

	# pdb.set_trace()
	# While there are unvisited cells
	while unvisited:
		# Get unvisited neighbors of current cell
		neighbor_list = find_unvisited_neighbors(current_cell,size,visited)

		# If there are unvisited neighbors
		if neighbor_list:
			# Select random neighbor
			neighbor = neighbor_list[random.randrange(0,sys.maxint) % len(neighbor_list)]

			# Push current cell onto the stack
			stack.append(current_cell)

			# Co-ordinates for convenience
			i = neighbor[0]
			j = neighbor[1]

			# Set blocked status
			grid[i][j] = determine_blocked_status()
			if i == 0 and j == 0:
				grid[i][j] = 'u'
			elif i == 100 and j == 100:
				grid[i][j] = 'u'

			# Make the chosen cell the current cell and mark it as visited
			if neighbor in unvisited:
				unvisited.remove(neighbor)
				visited.append(neighbor)
				current_cell = neighbor

		# If stack is not empty
		elif stack:
			current_cell = stack.pop()

	return grid

def tuples_to_objects(grid):
	size = len(grid)

	object_grid = [['x' for i in range(size)] for j in range(size)]
	for i in range(size):
		for j in range(size):
			object_grid[i][j] = Cell(i,j,size)
			object_grid[i][j].status = grid[i][j]
 
	return object_grid

def print_cells(grid):
	size = len(grid)

	for i in range(size):
		row = list()
		for j in range(size):
			row.append(grid[i][j].status)

		print row