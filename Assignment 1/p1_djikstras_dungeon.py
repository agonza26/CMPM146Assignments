from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop
# http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/117228
#from priodict import priorityDictionary




def navigation_edges(level, cell):

	steps = []

	x = cell[0]
	y = cell[1]

	for dx in[-1,0,1]:
		for dy in [-1,0,1]:
			next_cell = (x+ dx, y+dy)


			dist = sqrt(dx*dx+dy*dy)
			if(dist>0 and next_cell in level["spaces"]):
				steps.append(next_cell)
	return steps








def dijkstras_shortest_path(src, dst, graph, adj, boolean):
	dist = {}
	prev = {}
	Q = []



	dist[src] = 0
	prev[src] = None



 
	
	heappush(Q, (dist[src],src))


	while Q :
		
		distU, u = heappop(Q)
		
		



		if u == dst:
			break

		

		neightbors = navigation_edges(graph,u)
		

		for v in neightbors:
			
			alt = dist[u] + sqrt(abs( u[0] - v[0])*abs( u[0] - v[0]) +        abs( u[1] - v[1])*abs( u[1] - v[1]))
			


			
			if(v in dist):
				if( alt < dist[v] ):

					dist[v] = alt
					prev[v] = u
			else:
				dist[v] = alt
				prev[v] = u
				heappush( Q,(dist[v],v))
		

	S = []
	x = dst
	if(boolean):
		print dist[dst]

	while x in prev:
		heappush(S, x)
		x=prev[x]



	return S












def test_route(filename, src_waypoint, dst_waypoint,boolean):
	level = load_level(filename)
	show_level(level)
	src = level['waypoints'][src_waypoint]
	dst = level['waypoints'][dst_waypoint]
	path = dijkstras_shortest_path(src, dst, level, navigation_edges,boolean)
	if path:
		show_level(level, path)
	else:
		print "No path possible!"



#main method
if __name__ ==  '__main__':
	import sys

	if(len(sys.argv)<4):
		print("usage: python p1_djikstras_dungeon.py [filename] [waypoint 1] [waypoint 2] ")
		sys.exit()
	elif(len(sys.argv)==4):
		_, filename, src_waypoint, dst_waypoint = sys.argv
	else:

		 filename = sys.argv[1]
		 src_waypoint = sys.argv[2]
		 dst_waypoint = sys.argv[3]

	if len(sys.argv) >= 5:
		if sys.argv[4] == "true":
			flag = True
	else:
		flag = False

	test_route(filename, src_waypoint, dst_waypoint, flag)
