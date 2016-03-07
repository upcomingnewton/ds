import sys
import random
class Vertex(object):
    def __init__(self, key, color='White', distance=0, parent=None):
        self.key = key
        self.neighbours = dict()
        self.color = color
        self.distance = distance
        self.parent = parent
    
    def addNeighbour(self, nbr_key, wt=0):
        self.neighbours[nbr_key] = wt
    
    def getNeighbours(self):
        return self.neighbours.keys()
    
    def getNeighbourWeight(self, nbr_key):
        return self.neighbours.get(nbr_key, None)
    
    def __str__(self):
        return "{0}({1})".format(str(self.key),",".join([str(x.key) for x in self.neighbours]))

class Graph:
    def __init__(self):
        self.vertices = dict()
    
    def addVertex(self, key):
        if self.vertices.get(key) == None:
            v = Vertex(key)
            self.vertices[key] = v
        return self.vertices.get(key)
    
    def getVertices(self):
        return self.vertices.keys()
    
    def getVertex(self, key):
        return self.vertices.get(key)
    
    
    def addEdge(self,src,dest,wt=0):
        s = self.addVertex(src)
        d = self.addVertex(dest)
        s.addNeighbour(d,wt)
        d.addNeighbour(s,wt)
        
    def __iter__(self):
        return iter(self.vertices.values())
    
class PriorityQueue:
    def __init__(self):
        self.nums = list()
    
    def buildQueue(self, lnums):
        # build a min heap using lnums
        heap_size = len(lnums)
        self.nums = lnums[:]
        for i in range(heap_size/2,-1,-1):
            self.heapify(i,heap_size)
    
    def extractMin(self):
        # remove and return smallest num
        _min = self.nums[0]
        self.nums[0] = self.nums[-1]
        del self.nums[-1]
        self.heapify(0,len(self.nums))
        return _min
    
    def decreaseKey(self, key, new_prior):
        # decrease priority of key to new_prior
        idx = -1
        for (i,k) in enumerate(self.nums):
            if k[0] == key:
                idx = i
                break
        
        if idx != -1 and new_prior < self.nums[idx][1]:
            par = (idx-1)/2
            self.nums[idx][1] = new_prior
            while(par >= 0 and self.nums[par][1] > self.nums[idx][1]):
                self.nums[par], self.nums[idx] = self.nums[idx], self.nums[par]
                idx = par
                par = (idx-1)/2
        
    def insert(self, key, prior):
        # insert a new key with priority: prior
        self.nums.append([key,sys.maxsize])
        self.decreaseKey(len(self.nums)-1,prior)
    
    def heapify(self, idx, heap_size):
        smallest = idx
        left = 2*idx + 1
        right = 2*idx + 2
        if left < heap_size and self.nums[left][1] < self.nums[smallest][1]:
            smallest = left
        if right < heap_size and self.nums[right][1] <  self.nums[smallest][1]:
            smallest = right
        if smallest != idx:
            self.nums[smallest], self.nums[idx] = self.nums[idx], self.nums[smallest]
            self.heapify(smallest,heap_size)
    
    def isEmpty(self):
        return len(self.nums) == 0
    

def prim_mst(g,start):
    pq = PriorityQueue()
    for i in g:
        i.distance = sys.maxsize
        i.parent = None
    start.parent = None
    start.distance = 0
    pq.buildQueue([[v,v.distance] for v in g])
    while pq.isEmpty() == False:
        cur = pq.extractMin()[0]
        for n in cur.getNeighbours():
            new_cost = cur.distance + cur.getNeighbourWeight(n)
            if new_cost < n.distance:
                n.distance = new_cost
                n.parent = cur
                pq.decreaseKey(n,new_cost)
        

        
if __name__ == "__main__":
    sz = 10
    nums = range(sz)
    alphas = [chr(65 + i) for i in nums]
    prior = [random.choice(nums) for _ in nums]
    pq = PriorityQueue()
    print('Building Queue')
    pq.buildQueue([[a,p] for (a,p) in zip(alphas,prior)])
    print pq.nums
    print 'extractMin', pq.extractMin()
    print pq.nums
    print 'extractMin', pq.extractMin()
    print pq.nums
    print 'extractMin', pq.extractMin()
    print pq.nums
    print 'extractMin', pq.extractMin()
    print pq.nums
    print 'extractMin', pq.extractMin()
    print pq.nums
    print 'insert', pq.insert(chr(65 + sz+1),-10)
    print pq.nums
    print 'insert', pq.insert(chr(65 + sz+2),-20)
    print pq.nums
    print 'insert', pq.insert(chr(65 + sz+3),-11)
    print pq.nums
    print 'insert', pq.insert(chr(65 + sz+4),-13)
    print pq.nums
    print 'decreaseKey', pq.decreaseKey(4, -40)
    print pq.nums
    print 'decreaseKey', pq.decreaseKey(7, 0)
    print pq.nums
    
    def printg(g):
        for x in g:
            print x
    
    def print_par(g):
        print '-'*50
        for x in g:
            print x,x.distance,x.parent
        print '-'*50
        
    

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
    
    printg(g1)
    prim_mst(g1,g1.getVertex('a'))
    print_par(g1)
    
    g2 = Graph()
    g2.addEdge('a','b',10)
    g2.addEdge('a','d',5)
    g2.addEdge('a','e',3)
    g2.addEdge('b','c',9)
    g2.addEdge('b','d',12)
    g2.addEdge('c','d',2)
    g2.addEdge('d','e',7)
    
    printg(g2)
    prim_mst(g2,g2.getVertex('a'))
    print_par(g2)