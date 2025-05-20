import sys

from utils import gv, i_range

# The outgoing directions when a beam moving in a given direction hits a given object.
DIR_DELTAS = {
  '/': { (-1, 0): [(0, 1)], (0, 1): [(-1, 0)], (1, 0): [(0, -1)], (0, -1): [(1, 0)] },
  '\\': { (-1, 0): [(0, -1)], (0, 1): [(1, 0)], (1, 0): [(0, 1)], (0, -1): [(-1, 0)] },
  '|': { (0, 1): [(-1, 0), (1, 0)], (0, -1): [(-1, 0), (1, 0)] },
  '-': { (-1, 0): [(0, -1), (0, 1)], (1, 0): [(0, -1), (0, 1)] }
}

def count_energised(g, si, sj, di, dj):
  visited = set([(si, sj, di, dj)])
  q = [(si, sj, di, dj)]
  q_head = 0

  i, j = si, sj
  while q_head < len(q):
    i, j, di, dj = q[q_head]
    q_head += 1

    for (ndi, ndj) in DIR_DELTAS.get(g[i][j], {}).get((di, dj), [(di, dj)]):
      ni, nj = i + ndi, j + ndj
      if gv(g, ni, nj) != None and (ni, nj, ndi, ndj) not in visited:
        visited.add((ni, nj, ndi, ndj))
        q.append((ni, nj, ndi, ndj))

  return len(set((i, j) for i, j, _, _ in visited))

def solve(instream):
  g = [l[:-1] for l in instream.readlines()]
  print(count_energised(g, 0, 0, 0, 1))

if __name__ == '__main__':
  solve(sys.stdin)
