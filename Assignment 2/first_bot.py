import random
import math
def think(state, quip):
   
  return state.get_moves()[math.floor(random.random())*  len( state.get_moves())]
