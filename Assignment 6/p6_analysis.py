from p6_game import Simulator

ANALYSIS = {}
An = {}

def analyze(design):

	ANALYSIS.clear()
	An.clear()
	
	sim = Simulator(design)
	queue = []
	initS = sim.get_initial_state() #[0] = point [1] = powers
	moves = sim.get_moves()
	ANALYSIS[initS] = None
	An[initS[0]] = {initS[1]: None}
	
	queue.append(initS)	
	while queue:
		currS = queue.pop(0)
		for move in moves:
			nextS = sim.get_next_state(currS, move)
			if not nextS:
				continue
			elif nextS not in ANALYSIS:
				queue.append(nextS)
				ANALYSIS[nextS] = currS

				if nextS[0] not in An:
					An[nextS[0]] = {nextS[1]: currS}
				elif nextS[0] not in An[nextS[0]]:
					An[nextS[0]][nextS[1]] = currS
					

def inspect((i,j), draw_line):
	Ppoint = (i,j)
	offset = 0
	
	
	if Ppoint not in An:
		return None
	for powers in An[Ppoint]:
		state = (Ppoint, powers)
		offset += 0.1
		while state:
			if ANALYSIS[state]:
				draw_line(state[0], ANALYSIS[state][0], offset, state[1])
				state = ANALYSIS[state]
			else:
				break

	"""
	#old version
	for state in ANALYSIS:
		print times
		times += 1
		if state[0] == (i,j):
			offset += 0.1
			while state:
				if ANALYSIS[state]:
					draw_line(state[0], ANALYSIS[state][0], offset, state[1])
					state = ANALYSIS[state]
				else:
					break

	"""

