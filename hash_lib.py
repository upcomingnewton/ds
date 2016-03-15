import sys

def sax_hash(w):
  h = 0
  for x in w:
    h ^= ( h << 5 ) + ( h >> 2 ) + ord(x)
  return h

def djb_xor_hash(w):
  h = 0
  for x in w:
    h = 33*h ^ ord(x)
  return h

def djb_hash(w):
  h = 0
  for x in w:
    h = 33*h + ord(x)
  return h

def rotating_hash(w):
  h = 0
  for x in w:
    h = ( h << 4) ^ ( h >> 28) ^ ord(x)
  return h


def add_hash(w):
  h = 0
  for i in w:
    h += ord(i)
  return h

def xor_hash(w):
  h = 0
  for x in w:
    h = h ^ ord(x)
  return h

def get_words(file_path):
  f = open(file_path)
  w = [x.strip() for x in f.readlines()]
  f.close()
  return w

def test(fnx, words):
  # count # of collisions
  col = dict()
  n = len(words)
  ccol = 0
  lcol = dict()
  for w in words:
    h = fnx(w)
    if h in col:
      ccol += 1
      col[h].append(w)
      lcol[h] += 1
      #print 'COLLISION: ',col[h]
    else:
      col[h] = [w]
      lcol[h] = 1
  print "NUMBER OF COLLISIONS", ccol
  print "NUMBER OF BUCKETS GENERATED", len(col.keys())
  cols = sorted(lcol.values())
  print "BUCKET WITH MAX KEYS:", cols[-1], (float)(cols[-1]*100)/n,  " %age"
  print "BUCKET WITH MIN KEYS:", cols[0], (float)(cols[0]*100)/n,  " %age"
  return ccol
  #return (ccol, col)

if __name__ == "__main__":
  file_path = sys.argv[1]
  words = get_words(file_path)
  print "TESTING add_hash", test(add_hash, words)
  print "TESTING xor_hash", test(xor_hash, words)
  print "TESTING rotating_hash", test(rotating_hash, words)
  print "TESTING djb_hash", test(djb_hash, words)
  print "TESTING djb_xor_hash", test(djb_xor_hash, words)
  print "TESTING sax_hash", test(sax_hash, words)
