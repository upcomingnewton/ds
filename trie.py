class TrieNode:
    def __init__(self, key):
        self.key = key
        self.children = dict()
        self.is_ending = False
        self.value = None
        
    def __str__(self):
        return "{0}, {1}, {2}".format(str(self.key),str(self.is_ending),str(self.children))
    
    
    
class Trie(object):
    def __init__(self):
        self.root = TrieNode('$')
        self.size = 0
    
    def isEmpty(self):
        return len(self.root.children.keys()) == 0
    
    def lazy_size(self, node=None):
        c = 0
        if node ==  None:
            node = self.root
        if node.is_ending == True:
            c += 1
        for x in node.children.values():
            c += self.lazy_size(x)
        return c
    
    def find_prefix(self, key):
        print "[0]Prefix Searching: ", key
        node = self.root
        i = 0
        while i < len(key) and node.children.get(key[i]):
            node = node.children.get(key[i])
            i += 1
        print "[1]Prefix Searching: ", key[:i], "(",node,")"
        return (node,i)
    
    def search(self, key):
        print "[0]Searching: ", key
        (node,i) = self.find_prefix(key)
        print "[1]Searching: ", key[:i],  "(",node,")"
        return (node.is_ending == True \
                and i == len(key))
    
    def __contains__(self, key):
        return self.search(key)
    
    
    def insert(self, key, val=None):
        print "[0]INSERTING: ", key
        (node,i) = self.find_prefix(key)
        while i < len(key):
            x = key[i]
            node.children[x] = TrieNode(x)
            node = node.children[x]
            i += 1
        node.is_ending = True
        print "[1]INSERTING: ", key[:i],  "(",node,")"
        self.size += 1
        node.value = val
        return node
    
    def keysWithPrefix(self, key):
        node = self.root
        l = list()
        (node,i) = self.find_prefix(key)
        if node.is_ending == True:
            l = [(node,"")]
        for x in node.children.values():
            l.extend(self._keys(x,''))
        for x in l:
            print key + x[1]
        return l
    
    def keys(self):
        node = self.root
        l = list()
        for x in node.children.values():
            l.extend(self._keys(x,''))
        return l
    
    def _keys(self, node, prefix):
        l = list()
        if node.is_ending == True:
            l.extend([[node,prefix +  node.key]])
        for x in node.children.values():
            l.extend(self._keys(x,prefix + node.key))
        return l
    
    def delete(self, key):
        self._del(self.root,key)
    
    def _del(self,node,key):
        if len(key) == 1:
            if len(node.children[key[0]].children.keys()) > 0:
                node.children[key[0]].is_ending = False
                return False
            else:
                del node.children[key[0]]
                return not node.is_ending
        else:
            if( self._del(node.children[key[0]], key[1:]) == True):
                del node.children[key[0]]
            
            
if __name__ == "__main__":
    t = Trie()
    t.insert("bat")
    t.insert("by")
    t.insert("bye")
    t.insert("sea")
    t.insert("she")
    t.insert("sells")
    t.insert("shells")
    t.insert("the")
    t.insert("shore")
    print "keys\n"
    l = t.keys()
    for x in l:
        print x[0], x[1]
    t.keysWithPrefix('b')
    t.keysWithPrefix('she')