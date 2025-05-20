import sys

from day_16a import count_energised
from utils import i_range

def solve(instream):
  g = [l[:-1] for l in instream.readlines()]

  best = 0
  for si in i_range(g):
    best = max(best, count_energised(g, si, 0, 0, 1))
    best = max(best, count_energised(g, si, len(g[si])-1, 0, -1))
  for sj in i_range(g[0]):
    best = max(best, count_energised(g, 0, sj, 1, 0))
    best = max(best, count_energised(g, len(g)-1, sj, -1, 0))
  print(best)

if __name__ == '__main__':
  solve(sys.stdin)
