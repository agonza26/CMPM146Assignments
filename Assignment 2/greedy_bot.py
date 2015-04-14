from random import randint

def think(state, quip):
	bestMove = None
	bestScore = state.get_score()[state.get_whos_turn()] 

	#print state.get_score()[state.get_whos_turn()]
	for i in state.get_moves():
		stateCopy = state.copy()
		stateCopy.apply_move(i)

		if bestScore < stateCopy.get_score()[state.get_whos_turn()]:
			bestScore = stateCopy.get_score()[state.get_whos_turn()]
			bestMove = i 
			
	if bestMove == None:
		bestMove=state.get_moves()[  randint(0,len( state.get_moves())-1)  ]

	return bestMove

