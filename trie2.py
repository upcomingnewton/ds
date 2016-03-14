class TrieNode:
  def __init__(self, key):
    self.key = key
    self.value = None
    self.children = dict()
    self.is_ending = False
  
  def __str__(self):
    return "({0}, {1}, {2})".format(str(self.key), str(self.children), str(self.is_ending))
  def __repr__(self):
    return "({0}, {1}, {2})".format(str(self.key), str(self.children), str(self.is_ending))
    

class Trie:
  def __init__(self):
     self.root = TrieNode('$')

  def insert(self,key, val=None):
    (node,i) = self._longestPrefixOf(self.root, key, 0)
    for x in key[i:]:
      node.children[x] = TrieNode(x)
      node = node.children[x]
    node.is_ending = True

  def get(self, key):
    (node,i) = self._longestPrefixOf(self.root, key, 0)
    if i == len(key) and node.is_ending:
      return (node,i)
    else:
      return (None,-1)    

  def __contains__(self, key):
    x = self.get(key)
    return x[1] != -1

  def isEmpty(self):
    return len(self.root.keys()) == 0

  def tsize(self):
    c = 0
    for x in self.root.children.values():
      c += self._size(x)
    return c

  def _size(self,node):
    c = 0
    if node.is_ending == True:
      c += 1
    for x in node.children.values():
      c += self._size(x)
    return c    
  
  def keys(self):
    l = list()
    for x in self.root.children.values():
      l.extend(self._keys(x,''))
    return l
  
  def _keys(self, node, p):
    l = list()
    if node.is_ending == True:
      l.extend([(p + node.key,node)])
    p = p + node.key
    for x in node.children.values():
      l.extend(self._keys(x,p))  
    return l
  
  def longestPrefixOf(self, key):
    return self._longestPrefixOf(self.root, key, 0)
 
  def _longestPrefixOf(self, node, key, i):
    if i == len(key):
      return (node,i)
    if key[i] in node.children.keys():
      return self._longestPrefixOf(node.children[key[i]], key, i+1)
    return (node,i)
  
  def keysWithPrefix(self, key):
    (node,i) = self._longestPrefixOf(self.root,key,0)
    l = list()
    for x in node.children.values():
      l.extend(self._keys(x, key[:i]))
    return l

  def delete(self, key):
    self._del(self.root, key, 0)
  
  def _del(self, node, key, i): 
    if i == len(key)-1:
      # last node
      if (node.children[key[i]]) > 0:
        node.children[key[i]].is_ending = False
        return False
      else:
        del node.children[key[i]]
        return node.is_ending == False
    else:
      if key[i] in node.children.keys():
        res = self._del(node.children[key[i]], key, i+1)
        if res == True:
          del node.children[key[i]]
 

if __name__ == "__main__":
    t = Trie()
    print 'INSERT',"bat"
    t.insert("bat")
    print 'INSERT',"by"
    t.insert("by")
    print 'INSERT',"bye"
    t.insert("bye")
    print 'INSERT',"sea"
    t.insert("sea")
    print 'INSERT',"she"
    t.insert("she")
    print 'INSERT',"sells"
    t.insert("sells")
    print 'INSERT',"shells"
    t.insert("shells")
    print 'INSERT',"the"
    t.insert("the")
    print 'INSERT',"shore"
    t.insert("shore")
    print "keys\n"
    print "Size", t.tsize()
    l = t.keys()
    for x in l:
        print x
    print 'keysWithPrefix','b'
    l = t.keysWithPrefix('b')
    for x in l:
      print x
    print 'keysWithPrefix','she'
    l = t.keysWithPrefix('she')
    for x in l:
      print x
    print 'keysWithPrefix','sh'
    l = t.keysWithPrefix('sh')
    for x in l:
      print x
    print "get","batman",t.get("batman")
    print "get","shell",t.get("shell")
    print "get","shells",t.get("shells")
    print "get","shellsort",t.get("shellsort")
    print "get","bye",t.get("bye")
    print "longestPrefixOf","shellsort"
    print t.longestPrefixOf("shellsort")
    print 'DELETE','buay'
    t.delete('buay')
    l = t.keys()
    for x in l:
        print x
    print 'DELETE','shells'
    t.delete('shells')
    l = t.keys()
    for x in l:
        print x
    print 'DELETE','bye'
    t.delete('bye')
    print "Size", t.tsize()
    l = t.keys()
    for x in l:
        print x
    print "Size", t.tsize()
