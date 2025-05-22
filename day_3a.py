import sys
from collections import defaultdict

from utils import gv, i_range

# I've subsequently thought that using regexes would be a lot nicer here.

DIRS = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}

def solve(instream):
  grid = [[c for c in l[:-1]] for l in instream.readlines()]

  ns = defaultdict(list)
  for i in i_range(grid):
    start_j = None
    for j in i_range(grid[0]):
      if grid[i][j].isnumeric():
        start_j = start_j if start_j is not None else j
        ns[(i, start_j)].append(j)
      else:
        start_j = None

  good = [[False] * len(grid[0]) for _ in grid]
  for i in i_range(grid):
    for j in i_range(grid[0]):
      for di, dj in DIRS:
        if (lv := gv(grid, i + di, j + dj)) is not None and \
           lv != '.' and not lv.isnumeric():
          good[i][j] = True

  total = 0
  for (i, _), js in ns.items():
    if any(good[i][j] for j in js):
      total += int(''.join([grid[i][j] for j in js]))
  return total

if __name__ == '__main__':
  print(solve(sys.stdin))
