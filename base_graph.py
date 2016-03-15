
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

def getg1():
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
  return g1 
