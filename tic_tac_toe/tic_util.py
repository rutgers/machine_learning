from ticTreeNode import TicTreeNode
from copy import deepcopy
def win_board(b):
	'''
		Return:
			0 = not won
			1 = won by user
			2 = won by ai
	'''

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
	return not any(['u' in b for b in brd])

def is_legal(x, y, prevBoard):
	#print "x", x
	#print "y", y
	#print "prevBoard", prevBoard
	#if x < 0 or y < 0:
	#	print "negative indices"
	if x not in range(3) or y not in range(3):
		print "not in range"
		return False
	if prevBoard[x][y] == 'o' or prevBoard[x][y] == 'x':
		return False
	else:
		return True

def generateTree(player):
	base = [['u' for _ in range(3)] for _ in range(3)]
	root = TicTreeNode(base)
	generateTreeHelper(player, root)
	return root


def generateTreeHelper(player, root, depth = 0):
	#TODO put in condition where root is won
	if depth >= 9:
		return
	root.children = get_moves(root.board, player)
	for move in root.children:
		generateTreeHelper(not player, move, depth + 1)

#creates a list of possible next states after the current one
def get_moves(brd, player):
	moves = []
	p = 'x' if player else 'o'
	for a in range(3):
		for b in range(3):
			if is_legal(a, b, brd):
				new_brd = deepcopy(brd)#[[x for x in y] for y in brd]#brd
				#print new_brd
				new_brd[a][b] = p
				moves.append(TicTreeNode(new_brd))
	return moves


def minimax(nd, depth, player):
	#bestValue = 0
	if not depth or not nd.children:
		return nd.nodeValue
	f = max if player else min
	a = generateTree(1)
	printTree(a)
	return f(minimax(child, depth - 1, not player) for child in nd.children)

def printTree(root):
	if root is None:
		return
	for i in root.board:
		print i
	print "\n"
	for j in root.children:
		printTree(j)

def main():
	#a = [['x', 'u', 'o'], ['u', 'u', 'u'], ['u', 'u', 'u']]
	#prints out a board from the bottom row
	root = generateTree(True)
	n = root
	while n.children != []:
		n = n.children[0]
	print n.board


if __name__ == "__main__":
	main()
