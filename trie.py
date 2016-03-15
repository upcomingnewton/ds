class TrieNode:
	def __init__(self, key):
		self.key = key
		self.children = dict()
		self.is_ending = False
		self.value = None

	def __repr__(self):
		return "{0} {1}".format(str(self.key),str(self.children.keys()))

class Trie:
	def __init__(self):
		self.root = TrieNode('$')
	
	def longestPrefixOf(self, key):
		return self._longestPrefixOf(self.root, key, 0)

	def _longestPrefixOf(self, node, key, i):
		if i  == len(key):
			return (node, i)
		if key[i] in node.children.keys():
			return self._longestPrefixOf(node.children[key[i]], key, i+1)
		return (node,i)
				
	
	def insert(self, key):
		(node, i) = self._longestPrefixOf(self.root, key, 0)
		for x in key[i:]:
			node.children[x] = TrieNode(x)
			node = node.children[x]
		node.is_ending = True

	def get(self, key):
		(node, i) = self._longestPrefixOf(self.root, key, 0)
		if i == len(key) and node.is_ending == True:
			return node
		return None

	def isEmpty(self):
		return len(self.root.children.keys()) == 0	

	def delete(self, key):
		self._del(self.root, key, 0)	
	
	def _del(self, node, key, i):
		if len(key)-1 == i:
			if len(node.children[key[i]].children.keys()) > 0:
				node.children[key[i]].is_ending = False
				return False
			else:
				del node.children[key[i]]
				return node.is_ending == False
		if( self._del(node.children[key[i]],key,i+1) == True):
			del node.children[key[i]]		

	def keysWithPrefix(self, key):
		(node,i) = self._longestPrefixOf(self.root, key, 0)
		# we have found the node, which has key[i], there is no node with key[i+1]
		l = list()
		if i == len(key):
			for x in node.children.values():
				l.extend(self._keys(x,key))
		return l	

	def keys(self):
		l = list()
		for x in self.root.children.values():
			l.extend(self._keys(x,''))
		return l
	
	def _keys(self, node, p):
		l = list()
		p = p + node.key
		if node.is_ending == True:
			l.extend([p])
		for x in node.children.values():
			l.extend(self._keys(x,p))
		return l

	def size(self):
		return self._size(self.root)
			
	def _size(self, node):
		c = 0
		if node.is_ending == True:
			c += 1
		for x in node.children.values():
			c += self._size(x)
		return c

def print_keys(l):
	for x in l:
		print x

if __name__ == "__main__":
	t = Trie()
	print "isEmpty", t.isEmpty()
	print "size", t.size()
	print "INSERT the", t.insert("the")
	print "INSERT small", t.insert("small")
	print "INSERT shy", t.insert("shy")
	print "INSERT girl", t.insert("girl")
	print "size", t.size()
	print "INSERT sells", t.insert("sells")
	print "INSERT shells", t.insert("shells")
	print "KEYS", print_keys(t.keys())
	print "INSERT by", t.insert("by")
	print "INSERT sea", t.insert("sea")
	print "size", t.size()
	print "INSERT bye", t.insert("bye")
	print "longestPrefixOf shellshort", t.longestPrefixOf("shellsort")
	print "longestPrefixOf b", t.longestPrefixOf("b")
	print "size", t.size()
	print "longestPrefixOf bystandder", t.longestPrefixOf("bystandder")
	print "get girl",t.get("girl")
	print "KEYS", print_keys(t.keys())
	print "get shells", t.get("shells")
	print "get man", t.get("man")
	print "isEmpty", t.isEmpty()
	print "size", t.size()
        print "delete the", t.delete("the")
	print "size", t.size()
	print "delete shells", t.delete("shells")
	print "size", t.size()
	print "delete bye", t.delete("bye")		
	print "KEYS", print_keys(t.keys())
 	print  "KEYS with prefix: b", print_keys(t.keysWithPrefix('b'))	
 	print  "KEYS with prefix: s", print_keys(t.keysWithPrefix('s'))	
 	print  "KEYS with prefix: sh", print_keys(t.keysWithPrefix('sh'))	
