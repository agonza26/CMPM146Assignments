import time
from math import *
import random
THINK_DURATION = 1


def think(state, quip):

    t_start = time.time()
    t_deadline = t_start + THINK_DURATION

    iterations = 0

    rootnode = Node(state)



    while True:



        node = rootnode
        new_state = state.Clone()




        # Select
        while node.untried_moves == [] and node.childNodes != []: # node is fully expanded and non-terminal
            node = node.SelectChild()


            new_state.apply_move(node.move)




        # Expand
        if node.untriedMoves != []: # if we can expand (i.e. state/node is non-terminal)
            m = random.choice(node.untriedMoves) 
            new_state.apply_move(m)
            node = node.AddChild(m,new_state) # add child and descend tree

        # Rollout - this can often be made orders of magnitude quicker using a state.GetRandomMove() function
        while new_state.GetMoves() != []: # while state is non-terminal
            new_state.DoMove(random.choice(new_state.GetMoves()))

        # Backpropagate
        while node != None: # backpropagate from the expanded node and work back to the root node
            node.Update(new_state.GetResult(node.playerJustMoved)) # state is terminal. Update node with result from POV of node.playerJustMoved
            node = node.parent











        t_now = time.time()
        if t_now > t_deadline:
            break













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
        """ Use the UCB1 formula to select a child node. Often a constant UCTK is applied so we have
            lambda c: c.wins/c.visits + UCTK * sqrt(2*log(self.visits)/c.visits to vary the amount of
            exploration versus exploitation.
        """
        s = sorted(self.children.values(), key = lambda c: c.score/c.visits + sqrt(2*log(self.visits)/c.visits))[-1]
        return s

    def AddChild(self, s, m):
        """ Remove m from untriedMoves and add a new child node for this move.
            Return the added child node
        """
        n = Node(s, self,m)
        self.untried_moves.remove(m)
        self.children.push(n)
        return n



	def Update(self, result):
        """ Update this node - one additional visit and result additional wins. result must be from the viewpoint of playerJustmoved.
        """
        self.visits += 1
        self.score = result



	def dump(self): ...



def UctSearch(initial_state):
	rootnode = Node(initial_state)

def TreePolicy()