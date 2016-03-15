import sys
import random


class Vertex:
  def __init__(self,key,par=None,color="White",distance=0):
    self.key = key
    self.neighbours = dict()
    self.parent = par
    self.color = color
    self.distance = distance
    self.entry = 0
    self.exit = 0
  
  def addNeighbour(self, nbr, wt=0):
    self.neighbours[nbr] = wt
 
  def getNeighbours(self):
    return self.neighbours.keys()
  
  def getNeighbourWeight(self, nbr):
    return self.neighbours.get(nbr)
  
  def __str__(self):
    return "{0} ({1})".format(str(self.key),",".join([str(x.key) for x in self.neighbours]))

class Graph:
  def __init__(self):
    self.vertices = dict()

  def addVertex(self, key):
    if self.vertices.get(key) == None:
        self.vertices[key] = Vertex(key)
    return self.vertices.get(key)

  def getVertices(self):
    return self.vertices.keys()

  def getVertex(self, key):
    return self.vertices.get(key)

  def addEdge(self, src, des, wt=0):
    s = self.addVertex(src)
    d = self.addVertex(des)
    s.addNeighbour(d,wt)
    d.addNeighbour(s,wt)
  def __iter__(self):
    return iter(self.vertices.values())
class UnionFind:
	def __init__(self):
		self.nums = dict()
	
	def make_set(self, l):
		for x in l:
			self.nums[x] = -1
	def find(self, x):
		if isinstance(self.nums[x],int) and self.nums[x] < 0:
			return x
		self.nums[x] = self.find(self.nums[x])
		return self.nums[x]
	
	def union(self, x, y):
		x1 = self.find(x)
		y1 = self.find(y)
		if self.nums[x1] < self.nums[y1]:
			self.nums[x1] += self.nums[y1]
			self.nums[y1] = x1
		else:
			self.nums[y1] += self.nums[x1]
			self.nums[x1] = y1

def kruskal(g):
  v = [x for x in g]
  edges = sorted([[u,y,u.getNeighbourWeight(y)] for u in v for y in u.getNeighbours()], key=lambda x: x[2])
  uf = UnionFind()
  uf.make_set(v)
  for x in edges:
     u,y,wt = x[0],x[1],x[2]
     if uf.find(u) != uf.find(y):
	print "Adding Edge from {0} To {1} with Weight {2}".format(str(u), str(y), str(wt))
        uf.union(u,y)


if __name__ == "__main__":
  t = range(10)
  uf = UnionFind()
  uf.make_set(t)
  print uf.find(5)
  print uf.find(7)
  print uf.find(9)
  uf.union(3,4)
  uf.union(1,9)
  uf.union(4,9)
  print uf.nums
  print uf.find(3)
  print uf.find(4)
  uf.union(5,6)
  print uf.nums
  uf.union(2,8)
  print uf.nums
  print uf.find(6)
  print uf.find(4)
  uf.union(4,8)
  print uf.nums
  uf.union(2,7)
  print uf.nums
  uf.union(6,7)
  print uf.nums
  print uf.find(5)
  print uf.nums
  print uf.find(6)
  print uf.nums
  print uf.find(7)
  print uf.nums
  print uf.find(8)
  g1 = Graph()
  g1.addEdge('a','b',6)
  g1.addEdge('a','f',3)
  g1.addEdge('a','g',6)
  g1.addEdge('a','c',10)
  g1.addEdge('b','f',2)
  g1.addEdge('c','g',1)
  g1.addEdge('c','d',7)
  g1.addEdge('d','g',5)
  g1.addEdge('d','e',3)
  g1.addEdge('d','h',4)
  g1.addEdge('e','h',4)
  g1.addEdge('f','g',1)
  g1.addEdge('g','h',9) 
  for x in g1:
    print x
  kruskal(g1) 
