import sys
from collections import defaultdict

from utils import gv, i_range

# I've subsequently thought that using regexes would be a lot nicer here.

DIRS = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}

def solve(stdin):
  grid = [[c for c in l[:-1]] for l in stdin.readlines()]

  num_pos = defaultdict(list)
  num_starts: list[list[tuple[int, int] | None]] = [[None] * len(grid[0]) for _ in grid]
  for i in i_range(grid):
    start_j = None
    for j in i_range(grid[0]):
      if grid[i][j].isnumeric():
        start_j = start_j if start_j is not None else j
        num_pos[(i, start_j)].append(j)
        num_starts[i][j] = (i, start_j)
      else:
        start_j = None

  good = [[False] * len(grid[0]) for _ in grid]
  for i in i_range(grid):
    for j in i_range(grid[0]):
      for di, dj in DIRS:
        if (lv := gv(grid, i + di, j + dj)) is not None and \
           not lv.isnumeric() and lv != '.':
          good[i][j] = True

  part_nums = {}
  for (i, start_j), js in num_pos.items():
    if any(good[i][j] for j in js):
      part_nums[(i, start_j)] = int(''.join([grid[i][j] for j in js]))

  total = 0
  for i in i_range(grid):
    for j in i_range(grid[0]):
      if grid[i][j] != '*':
        continue

      adj_part_nums = set()
      for di, dj in DIRS:
        if (lv := gv(num_starts, i + di, j + dj)) is not None:
          adj_part_nums.add(lv)

      if len(adj_part_nums) == 2:
        n1, n2 = list(adj_part_nums)
        total += part_nums[n1] * part_nums[n2]

  print(total)

if __name__ == '__main__':
  solve(sys.stdin)
