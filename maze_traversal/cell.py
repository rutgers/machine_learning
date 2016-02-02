class Cell:

	def __init__(self,i=0,j=0,size=0):
		self.g_val = 1000000
		self.f_val = 1000000
		self.h_val = 0
		self.search_val = 0
		self.x = i
		self.y = j
		self.status = 'x'
		self.parent = None
		self.hash_value = (self.x * size) + self.y
		self.heap_val = None


	def equals(self,second):
		if self.x == second.x and self.y == second.y:
			return True
		else:
			return False

	def hash_val(self,size):
		self.hash_value = (size * self.x) + self.y
		return self.hash_value

