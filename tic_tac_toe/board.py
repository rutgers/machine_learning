
class Board:

	def __init__(self,config):
		self.utility = 0
		self.config = config
		self.children = list()

	def set_value(self,x,y,val):
		if x not in range(3) or y not in range(3):
			print "not in range"
			return False
		if self.config[x][y] == 'o' or self.config[x][y] == 'x':
			return False
		else:
			self.config[x][y] = val
			return True

	def display(self):
		size = len(self.config)

		for i in range(size):
			row = list()
			for j in range(size):
				row.append(self.config[i][j])

			print row

	def win(self):
		'''
			Return:
				0 = not won
				1 = won by user
				2 = won by ai
		'''

		b = self.config

		if b[0][0] == b[0][1] == b[0][2]:
			if b[0][0] == 'x':
				return 1
			if b[0][0] == 'o':
				return 2
		if b[1][0] == b[1][1] == b[1][2]:
			if b[1][0] == 'x':
				return 1
			if b[1][0] == 'o':
				return 2
		if b[2][0] == b[2][1] == b[2][2]:
			if b[2][0] == 'x':
				return 1
			if b[2][0] == 'o':
				return 2
		if b[0][0] == b[1][0] == b[2][0]:
			if b[0][0] == 'x':
				return 1
			if b[0][0] == 'o':
				return 2
		if b[0][1] == b[1][1] == b[2][1]:
			if b[0][1] == 'x':
				return 1
			if b[0][1] == 'o':
				return 2
		if b[0][2] == b[1][2] == b[2][2]:
			if b[0][2] == 'x':
				return 1
			if b[0][2] == 'o':
				return 2
		if b[0][0] == b[1][1] == b[2][2]:
			if b[0][0] == 'x':
				return 1
			if b[0][0] == 'o':
				return 2
		if b[0][2] == b[1][1] == b[2][0]:
			if b[0][2] == 'x':
				return 1
			if b[0][2] == 'o':
				return 2
		else:
			return 0




	def stalemate(brd):
		'Insert logic for stalemate conditions'
		return not any(['u' in x for x in brd])
