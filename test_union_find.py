import sys

def test_union_find(cuf):
  t = [ 'v' + str(x) for x in range(10)]
  uf = cuf.UnionFind()
  uf.make_set(t)
  print uf.find('v5')
  print uf.find('v7')
  print uf.find('v9')
  uf.union('v3','v4')
  uf.union('v1','v9')
  uf.union('v4','v9')
  print uf.nums
  print uf.find('v3')
  print uf.find('v4')
  uf.union('v5','v6')
  print uf.nums
  uf.union('v2','v8')
  print uf.nums
  print uf.find('v6')
  print uf.find('v4')
  uf.union('v4','v8')
  print uf.nums
  uf.union('v2','v7')
  print uf.nums
  uf.union('v6','v7')
  print uf.nums
  print uf.find('v5')
  print uf.nums
  print uf.find('v6')
  print uf.nums
  print uf.find('v7')
  print uf.nums
  print uf.find('v8')
  print uf.find('v9')
  print uf.nums

if __name__ == "__main__":
  path = sys.argv[1].split('.')[0]
  cuf = __import__(path)
  test_union_find(cuf)	
