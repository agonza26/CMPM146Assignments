import time
import math
import random
THINK_DURATION = 1


def think(state, quip):

    t_start = time.time()
    t_deadline = t_start + THINK_DURATION

    iterations = 0

    rootnode = Node(state)



    while True:



        node = rootnode
        new_state = state.copy()
        iterations += 1



        # Select
        while node.untried_moves == [] and node.children != []: # node is fully expanded and non-terminal
            node = node.SelectChild()
            new_state.apply_move(node.move)





        # Expand
        if node.untried_moves != []: # if we can expand (i.e. state/node is non-terminal)
            m = random.choice(node.untried_moves) 
            new_state.apply_move(m)
            node = node.AddChild(new_state,m) # add child and descend tree







        # Rollout - this can often be made orders of magnitude quicker using a state.GetRandomMove() function
        while new_state.get_moves() != []: # while state is non-terminal
            new_state.apply_move(random.choice(new_state.get_moves()))

        # Backpropagate
        while node != None: # backpropagate from the expanded node and work back to the root node

        	me =0 
        	you = 1 
        	names = new_state.get_score().keys()
      

        	if (names[0] != node.who):
        		me =1
        		you = 0

        	node.Update( new_state.get_score()[names[me]] - new_state.get_score()[names[you]] )
        	node = node.parent











        t_now = time.time()
        if t_now > t_deadline:
            break

    sample_rate = float(iterations)/(t_now - t_start)
    #print iterations
    #$print sample_rate
    return sorted(rootnode.children, key = lambda c: c.visits)[-1].move
  










class Node(object):
	def __init__(self, state, move = None, parent=None):
		self.move = move
		self.parent = parent
		self.who = state.get_whos_turn()
		self.children = []
		self.untried_moves = state.get_moves()
		self.visits = 0
		self.score = 0.0

	def SelectChild(self):
		s = sorted(self.children, key = lambda c: c.score/c.visits + math.sqrt(2*math.log(self.visits)/c.visits))[-1]
		return s

	def AddChild(self, s, m):
		n = Node(s, m,self)
		self.untried_moves.remove(m)
		self.children.append(n)
		return n

	def Update(self, result):
		self.visits += 1
		self.score = result