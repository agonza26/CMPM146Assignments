from random import randint

def think(state, quip):
 # print len( state.get_moves())
  #print state.get_moves() 
  return state.get_moves()[  randint(0,len( state.get_moves())-1)  ]
