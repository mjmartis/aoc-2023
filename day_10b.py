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

LEFT_OF = {
  '|': {(1, 0): [(0, 1)], (-1, 0): [(0, -1)]},
  'L': {(1, 0): [], (0, -1): [(1, 0), (0, -1)]},
  'F': {(-1, 0): [(0, -1), (-1, 0)], (0, -1): []},
  '-': {(0, 1): [(-1, 0)], (0, -1): [(1, 0)]},
  'J': {(0, 1): [], (1, 0): [(0, 1), (1, 0)]},
  '7': {(0, 1): [(-1, 0), (0, 1)], (-1, 0): []},
}

def find_cycle(g, i, j, di, dj):
  cs = {}
  
  while True:
    i, j = i + di, j + dj
    cs[(i, j)] = (di, dj)

    if g.get((i, j), None) == 'S':
      return cs

    dirv = NEXT_DIR.get(g.get((i, j), None), {}).get((di, dj), None)
    if not dirv:
      return None

    di, dj = dirv

def mark_region(g, cs):
  reg = set()

  # Mark all cells to our left as we traverse the cycle.
  for (i, j), (di, dj) in cs.items():
    for di, dj in LEFT_OF.get(g.get((i, j), None), {}).get((di, dj), []):
      ni, nj = i+di, j+dj
      if (ni, nj) in g and (ni, nj) not in cs:
        reg.add((ni, nj))
  
  # Mark other cells connected to marked cells.
  q = list(reg)
  q_head = 0
  while q_head < len(q):
    i, j = q[q_head]
    q_head += 1

    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      ni, nj = i+di, j+dj
      if (ni, nj) in g and (ni, nj) not in cs and (ni, nj) not in reg:
        reg.add((ni, nj))
        q.append((ni, nj))

  return reg

def solve(instream):
  si, sj = None, None
  g = {}
  for i, l in enumerate(instream.readlines()):
    if (j := l.find('S')) > -1:
      si, sj = i, j

    # Cheeky: last col is always outside the cycle.
    for j, c in enumerate(l[:-1]+'.'):
      g[(i, j)] = c
  gh, gw = i+1, j+1  # pyright: ignore

  for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
    cycle = find_cycle(g, si, sj, di, dj)
    if cycle is None:
      continue

    reg = mark_region(g, cycle)
    if (0, gw-1) in reg:
      return gh * gw - len(reg) - len(cycle)
    return len(reg)

if __name__ == '__main__':
  print(solve(sys.stdin))
