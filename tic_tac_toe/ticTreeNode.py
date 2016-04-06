
class TicTreeNode:
	def __init__(self, board, children = []):
		self.board = board
		self.children = children
		self.nodeValue = 0 #This is a placeholder value to be set hopefully if
		#children is empty
