class UnionFind:
	def __init__(self):
		self.nums = dict()
	
	def make_set(self, l):
		for x in l:
			self.nums[x] = -1

	def find(self, x):
		if isinstance(self.nums[x], int) and self.nums[x] < 0:
			return x
		self.nums[x] = self.find(self.nums[x])
		return self.nums[x]

	def union(self, x, y):
		x1 = self.find(x)
		y1 = self.find(y)
		if self.nums[x1] <= self.nums[y1]:
			self.nums[x1] += self.nums[y1]
			self.nums[y1] = x1
		else:
			self.nums[y1] += self.nums[x1]
			self.nums[x1] = y1
	
if __name__ == "__main__":
  t = [ 'v' + str(x) for x in range(10)]
  uf = UnionFind()
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
