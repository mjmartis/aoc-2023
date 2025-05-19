import sys

from utils import gT, i_range

def find_diff(g, d):
  # Try splitting between each i and i+1.
  for i in i_range(g[0], o=-1):
    lefts = [[e for e in r[:i+1]] for r in g]
    rights = [[e for e in r[i+1:]] for r in g]

    diffs = 0
    for (l, r) in zip(lefts, rights):
      diffs += sum(1 for u, v in zip(l[::-1], r) if u != v)

    if diffs == d:
      return i+1
  
  return 0 

def solve(instream, d):
  total = 0

  while True:
    g = []
    while l := instream.readline()[:-1]:
      g.append([c for c in l])
    
    if not g:
      break

    total += find_diff(g, d) + 100 * find_diff(gT(g), d)
  
  print(total)

if __name__ == '__main__':
  solve(sys.stdin, 1)
