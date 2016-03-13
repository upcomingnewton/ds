from graph_base import g1, g2, g3, printg
import sys

def bellman_ford(g,s):
  v = [x for x in g]
  for x in v:
    x.distance = sys.maxsize
    x.parent = None
  s.distance = 0
  for i in range(len(v)):
    for u in v:
      for y in u.getNeighbours():
        if y.distance > u.distance + u.getNeighbourWeight(y):
          y.distance = u.distance + u.getNeighbourWeight(y)
          y.parent = u  
  printgg(g)
  for u in v:
    for y in u.getNeighbours():
      if y.distance > u.distance + u.getNeighbourWeight(y):
        return False
  return True

def printgg(g):
  for x in g:
    print x, x.distance, x.parent

if __name__ == "__main__":
   g1 = g1()
   print "g1",bellman_ford(g1,g1.getVertex('a'))
   print '-'*60
   g2 = g2()
   print "g2",bellman_ford(g2,g2.getVertex('s'))
   print '-'*60
   g3 = g3()
   print "g3",bellman_ford(g3,g3.getVertex('s'))
   print '-'*60
   
