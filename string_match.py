import sys
import random


def naive_matching(text, pattern):
	c = []
	for i in xrange(len(text)-len(pattern)):
		found = True
		for j in xrange(len(pattern)):
			if text[i+j] != pattern[j]:
				found = False
				break
		if found == True:
			c.append(i)
	return c
		
	

def RabinKarpMatcher(text, pattern):
	def _match(str1, str2,i):
		for j in xrange(len(str2)):
			if str1[i+j] != str2[j]:
				return False
		return True

	d = 257
	q = 11
	n = len(text)
	m = len(pattern)
	hp = 0
	ht = 0
	h = pow(d,m-1)%q
	c = list()
	for i in xrange(m):
		hp = (hp*d + ord(pattern[i]))%q
		ht = (ht*d + ord(text[i]))%q
	if _match(text,pattern,i) == True:
		c.append(i)
	for i in xrange(m,n):
		ht = (ht - ord(text[i-m])*h)%q
		ht = (ht*d + ord(text[i]))%q
		ht = (ht+q)%q	
		if _match(text,pattern,i) == True:
			c.append(i)
	return c

def test(fnx,text,pattern):
  off =  fnx(text,pattern)
  for x in off:
	print text[x:len(pattern)+x]

if __name__ == "__main__":
	pattern = sys.argv[1]
	text_file = sys.argv[2]
	ftext = open(text_file)
	text = ftext.read()
	ftext.close()
	#print 'Navie',test(naive_matching,text,pattern)
	#print 'RabinKarpMatcher',test(RabinKarpMatcher,text,pattern)
	print 'RabinKarpMatcher',test(RabinKarpMatcher,"3141592653589793","26")
	print 'RabinKarpMatcher',test(RabinKarpMatcher,"31415926535897926","26")
