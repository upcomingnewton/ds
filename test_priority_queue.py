import random
import sys

def test_priority_queue(cls):
	l = range(10)
	chrs = [chr(65+i) for i in l]
	pr = [-1*i for i in l]
	allc = [[y,x] for (x,y) in zip(chrs,pr)]
	pq = cls.PriorityQueue()
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

if __name__ == "__main__":
  path = sys.argv[1].split('.')[0]
  cls = __import__(path)
  test_priority_queue(cls)
