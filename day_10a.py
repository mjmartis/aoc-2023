import sys

from utils import i_range

NEXT_DIR = {
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

    gv = g.get((i, j), None)
    if gv == 'S':
      return step_count

    dirv = NEXT_DIR.get(gv, {}).get((di, dj), None)
    if not dirv:
      return None

    di, dj = dirv
    

def solve(instream):
  si, sj = None, None
  g = {}
  for i, l in enumerate(instream.readlines()):
    if (f := l.find('S')) > -1:
      si, sj = i, f
    for j in i_range(l, buf=-1):
      g[(i, j)] = l[j]

  for di, dj in [(1, 0), (-1, 0), (0, 1), (-1, 0)]:
    if (res := cycle_len(g, si, sj, di, dj)) is not None:
      return res // 2

if __name__ == '__main__':
  print(solve(sys.stdin))
