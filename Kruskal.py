class Vertex:
  def __init__(self, key, color="White", distance=0, parent=None):
    self.key = key
    self.neighbours = dict()
    self.color = color
    self.distance = distance
    self.parent = parent
    self.rank = -1
 
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
    if not self.vertices.get(key):
      self.vertices[key] = Vertex(key)
    return self.vertices.get(key)

  def getVertex(self, key):
    return self.vertices.get(key)

  def getVertices(self):
    return self.vertices.values()

  def addEdge(self,sr,de,wt=0):
    s = self.addVertex(sr)
    d = self.addVertex(de)
    s.addNeighbour(d,wt)
    d.addNeighbour(s,wt)

  def __iter__(self):
    return iter(self.vertices.values())

class FindUnion:
  def __init__(self):
    pass

  def make_set(self, v):
    for x in v:
      x.rank = 0
      x.parent = x

  def find_set(self, v):
    if v.parent != v:
      v.parent = self.find_set(v.parent)
    return v.parent

  def union(self, u, v):
    a = self.find_set(u)
    b = self.find_set(v)
    self.link(a,b)
 
  def link(self, u, v):
    if u.rank > v.rank:
      v.parent = u
      u.rank += v.rank
    else:
      u.parent = v
      v.rank += u.rank

def kruskal(g):
  uf = FindUnion()
  uf.make_set([v for v in g])
  edges = [(v,u,v.getNeighbourWeight(u)) for v in g for u in v.getNeighbours()]
  edges = sorted(edges, key=lambda x: x[2])
  print [x[2] for x in edges]
  tree = set()
  for x in edges:
    if uf.find_set(x[0]) != uf.find_set(x[1]):
      tree.add(x)
      print 'Adding..',x[0],x[1],x[2]
      uf.union(x[0],x[1])
  return tree

if __name__ == "__main__":
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
  
  for x in g1:
    print x
  edges = kruskal(g1)
  for x in edges:
    print str(x[0]), str(x[1]), x[2]
  for x in g1:
    print x.parent, x.rank
