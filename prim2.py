import sys

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

class PriorityQueue(object):
    def __init__(self):
      self.nums = list()

    def minHeapify(self, idx, hsize):
      smallest = idx
      left = 2*idx + 1
      right = 2*idx + 2
      if left < hsize and self.nums[left][0] < self.nums[smallest][0]:
        smallest = left
      if right < hsize and self.nums[right][0] < self.nums[smallest][0]:
        smallest = right
      if smallest != idx:
        self.nums[smallest], self.nums[idx] = self.nums[idx], self.nums[smallest]
        self.minHeapify(smallest, hsize)

    def buildQueue(self, l):
      self.nums = l[:]
      for i in range(len(l)/2,-1,-1):
        self.minHeapify(i,len(l))

    def extractMin(self):
      _min = self.nums[0]
      self.nums[0] = self.nums[-1]
      del self.nums[-1]
      self.minHeapify(0,len(self.nums))
      return _min
    
    def heap_sort(self):
      l = []
      while self.isEmpty() == False:
        l.append(self.extractMin())
      return l

    def decreaseKey(self, key, newk):
      idx = -1
      for (i,x) in enumerate(self.nums):
        if x[1] == key:
          idx = i
      if idx != -1 and newk < self.nums[idx][0]:
        self.nums[idx][0] = newk
        par = (idx-1)/2
        while par >= 0 and self.nums[par][0] > self.nums[idx][0]:
          self.nums[idx],self.nums[par] = self.nums[par],self.nums[idx]
          idx = par
          par = (idx-1)/2
        return True
      return False
    def isEmpty(self):
        return len(self.nums) == 0 

def prim(g,s):
  for x in g:
    x.parent = None
    x.distance = sys.maxsize 
  s.distance = 0
  s.parent = None
  pq = PriorityQueue()
  pq.buildQueue([[x.distance,x] for x in g])
  print pq.nums
  while pq.isEmpty() == False:
    cur = pq.extractMin()[1]
    for v in cur.getNeighbours():
      if cur.getNeighbourWeight(v) < v.distance:
        if pq.decreaseKey(v,cur.getNeighbourWeight(v)) == True:
          v.distance = cur.getNeighbourWeight(v)
          v.parent = cur


if __name__ == "__main__":
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
    
    ch = []
    for i in range(10):
      ch.append([10*i-100*i,chr(65+i)])
    pq = PriorityQueue()
    pq.buildQueue(ch)
    print pq.heap_sort()
    prim(g1,g1.getVertex('a'))
    for x in g1:
      print x.key, x.distance, x.parent
