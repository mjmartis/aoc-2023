import sys

from utils import i_range

DELTA = {
  '|': {(1, 0): (1, 0), (-1, 0): (-1, 0)},
  'L': {(1, 0): (0, 1), (0, -1): (-1, 0)},
  'F': {(-1, 0): (0, 1), (0, -1): (1, 0)},
  '-': {(0, 1): (0, 1), (0, -1): (0, -1)},
  'J': {(0, 1): (-1, 0), (1, 0): (0, -1)},
  '7': {(0, 1): (1, 0), (-1, 0): (0, -1)},
}

def cycle_len(g, i, j, di, dj):
  step_count = 0

  while True:
    i, j = i + di, j + dj
    step_count += 1

    if (i, j) not in g:
      return None

    if g[(i, j)] == 'S':
      return step_count

    if g[(i, j)] not in DELTA:
      return None

    lookup = DELTA[g[(i, j)]].get((di, dj), None)
    if not lookup:
      return None

    di, dj = lookup
    

def solve(instream):
  si, sj = None, None
  g = {}
  for i, l in enumerate(instream.readlines()):
    f = l.find('S')
    if f > -1:
      si, sj = i, f
    for j in i_range(l, buf=-1):
      g[(i, j)] = l[j]

  for di, dj in [(1, 0), (-1, 0), (0, 1), (-1, 0)]:
    res = cycle_len(g, si, sj, di, dj)
    if res is not None:
      print(res // 2)
      break

if __name__ == '__main__':
  solve(sys.stdin)
