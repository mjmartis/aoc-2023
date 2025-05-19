import sys
from collections import defaultdict
from itertools import product

from utils import gT, i_range

SKIP_LEN = int(1e6)

def dists_for_leading_dim(g, skip_len):
  gs = defaultdict(set)
  for i, j in product(i_range(g), i_range(g[0])):
    if g[i][j] == '#':
      gs[i].add(j)

  off, cs = 0, []
  for i in i_range(g):
    if i not in gs:
      off += skip_len - 1
    for j in gs[i]:
      cs.append(i + off)

  return sum(abs(u-v) for u, v in product(cs, cs))

def solve(instream, skip_len):
  g = [[c for c in l[:-1]] for l in instream.readlines()]

  total = dists_for_leading_dim(g, skip_len)
  total += dists_for_leading_dim(gT(g), skip_len)
  print(total // 2)

if __name__ == '__main__':
  solve(sys.stdin, SKIP_LEN)
