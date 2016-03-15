from union_find2 import UnionFind
from base_graph import getg1

def kruskal(g):
  v = [x for x in g]
  edges = sorted( [[u,y,u.getNeighbourWeight(y)] for u in v for y in u.getNeighbours()]  , key=lambda x: x[2])
  uf = UnionFind()
  uf.make_set(v)
  for x in edges:
    if uf.find(x[0]) != uf.find(x[1]):
      print 'Adding Edge from {0} to {1} with weight {2}'.format(x[0].key, x[1].key, x[2])
      uf.union(x[0],x[1])

if __name__ == "__main__":
  kruskal(getg1())
