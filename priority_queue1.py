class PriorityQueue:
	def __init__(self):
		self.nums = list()
	
	def buildQueue(self, l):
		n = len(l)
		self.nums = l[:]
		for i in range(n/2, -1, -1):
			self.minHeapify(i,n)

	def extractMin(self):
		_min = self.nums[0]
		self.nums[0] = self.nums[-1]
		del self.nums[-1]
		self.minHeapify(0,len(self.nums))
		return _min

	def decreaseKey(self, key, newval):
		i = -1
		for (j,x) in enumerate(self.nums):
			if x[1] == key:
				i = j
				break
		if i != -1:
			par = (i-1)/2
			self.nums[i][0] = newval
			while par >= 0 and self.nums[par][0] > self.nums[i][0]:
				self.nums[par],self.nums[i] = self.nums[i], self.nums[par]
				i = par
				par = (par-1)/2

	def isEmpty(self):
		return len(self.nums) == 0

	def minHeapify(self, i, heapsize):
		smallest = i
		left = 2*i + 1
		right = 2*i + 2
		if left < heapsize and self.nums[left][0] < self.nums[smallest][0]:
			smallest = left
		if right < heapsize and self.nums[right][0] < self.nums[smallest][0]:
			smallest = right
		if smallest != i:
			self.nums[smallest],self.nums[i] = self.nums[i], self.nums[smallest]
			self.minHeapify(smallest,heapsize)

if __name__ == "__main__":
	l = range(10)
	chrs = [chr(65+i) for i in l]
	pr = [-1*i for i in l]
	allc = [[y,x] for (x,y) in zip(chrs,pr)]
	pq = PriorityQueue()
	pq.buildQueue(allc)
	while pq.isEmpty() == False:
		import random
		print pq.nums
		n = [x[1] for x in pq.nums]
		x = random.choice(n)
		print pq.extractMin()
		print pq.nums
	        newv = -1*random.randint(0,100)	
		print 'decreaseKey',x,newv,pq.decreaseKey(x,newv)
