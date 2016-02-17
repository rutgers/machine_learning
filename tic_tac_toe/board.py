class Board:

	def __init__(self,config):
		self.utility = 0
		self.config = config
		self.children = list()

	def set_value(self,x,y,val):
		self.config[x][y] = val

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
			elif b[0][0] == 'u':
				return 2
		elif b[1][0] == b[1][1] == b[1][2]:
			if b[1][0] == 'x':
				return 1
			elif b[1][0] == 'u':
				return 2
		elif b[2][0] == b[2][1] == b[2][2]:
			if b[2][0] == 'x':
				return 1
			elif b[2][0] == 'u':
				return 2
		elif b[0][0] == b[1][0] == b[2][0]:
			if b[0][0] == 'x':
				return 1
			elif b[0][0] == 'u':
				return 2
		elif b[0][1] == b[1][1] == b[2][1]:
			if b[0][1] == 'x':
				return 1
			elif b[0][1] == 'u':
				return 2
		elif b[0][2] == b[1][2] == b[2][2]:
			if b[0][2] == 'x':
				return 1
			elif b[0][2] == 'u':
				return 2
		elif b[0][0] == b[1][1] == b[2][2]:
			if b[0][0] == 'x':
				return 1
			elif b[0][0] == 'u':
				return 2
		elif b[0][2] == b[1][1] == b[2][0]:
			if b[0][2] == 'x':
				return 1
			elif b[0][2] == 'u':
				return 2
		else:
			return 0




	def stalemate(self):
		'Insert logic for stalemate conditions'