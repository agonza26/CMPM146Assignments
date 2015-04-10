import random
import math
def think(state, quip):
  
  return state.get_moves()[  (int)(math.floor(random.random() *  len( state.get_moves())))   ]
