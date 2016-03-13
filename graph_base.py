


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

  def __iter__(self):
    return iter(self.vertices.values())

def g1():
  g1 = Graph()
  g1.addEdge('a','b',7)
  g1.addEdge('a','d',5)
  g1.addEdge('b','c',8)
  g1.addEdge('b','d',9)
  g1.addEdge('b','e',7)
  g1.addEdge('c','e',5)
  g1.addEdge('d','e',15)
  g1.addEdge('d','f',6)
  g1.addEdge('e','f',8)
  g1.addEdge('e','g',9)
  g1.addEdge('f','g',11)
  return g1

def g2():
  g2 = Graph()
  g2.addEdge('s','a',3)
  g2.addEdge('s','c',5)
  g2.addEdge('s','e',2)
  g2.addEdge('a','b',-4)
  g2.addEdge('b','g',4)
  g2.addEdge('c','d',6)
  g2.addEdge('d','g',8)
  g2.addEdge('d','c',-3)
  g2.addEdge('e','f',3)
  g2.addEdge('f','e',-6)
  g2.addEdge('f','g',7)
  return g2
  
  
def g3():
  g3 = Graph()
  g3.addEdge('s','t',3)
  g3.addEdge('s','y',5)
  g3.addEdge('t','x',6)
  g3.addEdge('t','y',2)
  g3.addEdge('y','z',6)
  g3.addEdge('y','t',1)
  g3.addEdge('y','x',4)
  g3.addEdge('x','z',2)
  g3.addEdge('z','x',7)
  g3.addEdge('z','s',3)
  return g3

def printg(g):
  for x in g:
    print x

if  __name__ == "__main__":
  printg(g1())
  print '-'*50
  printg(g2())
  print '-'*50
  printg(g3())
  print '-'*50
  
