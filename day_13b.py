import sys

from utils import gT

def find_diff(g, d):
  # Try splitting between each i and i+1.
  for i in range(len(g[0])-1):
    lefts = [[e for e in r[:i+1]] for r in g]
    rights = [[e for e in r[i+1:]] for r in g]

    diffs = []
    for (l, r) in zip(lefts, rights):
      diffs.append(sum(1 for u, v in zip(l[::-1], r) if u != v))

    if sum(diffs) == d:
      return i+1
  
  return 0 

def solve(instream):
  total = 0

  while True:
    g = []
    while l := instream.readline()[:-1]:
      g.append([c for c in l])
    
    if not g:
      break

    total += find_diff(g, 1) + 100 * find_diff(gT(g), 1)
  
  print(total)

if __name__ == '__main__':
  solve(sys.stdin)
