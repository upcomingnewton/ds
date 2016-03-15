from base_graph import getg1
from priority_queue1 import PriorityQueue
import sys
def prim(g,s):
	for x in g:
		x.distance = sys.maxsize
		x.parent = None
		x.color = "White"
	s.distance = 0
	s.parent = 0
	pq = PriorityQueue()
	pq.buildQueue([[x.distance,x] for x in g])
	while pq.isEmpty() == False:
		cur = pq.extractMin()[1]
		cur.color = "Black"
		for x in cur.getNeighbours():
			if x.distance > cur.getNeighbourWeight(x) and x.color == "White":
				x.parent = cur
				x.distance = cur.getNeighbourWeight(x)
				pq.decreaseKey(x,x.distance)

if __name__ == "__main__":
  g = getg1()
  prim(g,g.getVertex('a'))
  for x in g:
    print x.key, x.distance, x.parent
