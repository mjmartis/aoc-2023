import sys
from collections import defaultdict

# I've subsequently thought that using regexes would be a lot nicer here.

DIRS = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}

def v(g, i, j):
  if 0 <= i < len(g) and 0 <= j < len(g[0]):
    return g[i][j] != '.' and not g[i][j].isnumeric()
  return False

def solve(instream):
  grid = [[c for c in l[:-1]] for l in instream.readlines()]

  ns = defaultdict(list)
  for i in range(len(grid)):
    start_j = None
    for j in range(len(grid[0])):
      if grid[i][j].isnumeric():
        start_j = start_j if start_j is not None else j
        ns[(i, start_j)].append(j)
      else:
        start_j = None

  good = [[False] * len(grid[0]) for _ in grid]
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      for di, dj in DIRS:
        if v(grid, i + di, j + dj):
          good[i][j] = True

  total = 0
  for (i, _), js in ns.items():
    if any(good[i][j] for j in js):
      total += int(''.join([grid[i][j] for j in js]))
  print(total)

if __name__ == '__main__':
  solve(sys.stdin)
