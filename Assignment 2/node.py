




class Node(object):
	def __init__(self, state, parent=None):
		self.parent = parent
		self.who = state.get_whos_turn()
		self.children = {}
		self.untried_moves = state.get_moves()
		self.visits = 0
		self.score = 0.0

	def dump(self): ...
