import sys
from queue import PriorityQueue

from utils import gv

def solve(instream):
  g = [[int(v) for v in l[:-1]] for l in instream.readlines()]

  costs = {}
  q = PriorityQueue()
  q.put((0, 0, 0, 0, 1, 3))
  q.put((0, 0, 0, 1, 0, 3))
  while not q.empty():
    (cost, i, j, di, dj, rem_steps) = q.get()

    if (i, j, di, dj, rem_steps) in costs:
      continue
    costs[(i, j, di, dj, rem_steps)] = cost

    for (ndi, ndj, ns) in [(di, dj, rem_steps-1), (dj, di, 2), (-dj, -di, 2)]:
      ni, nj = i + ndi, j + ndj
      if (dc := gv(g, ni, nj)) != None and (ni, nj, ndi, ndj, ns) not in costs and ns >= 0:
        q.put((cost + dc, ni, nj, ndi, ndj, ns))

  return min(v for (i, j, _, _, _), v in costs.items() if i == len(g)-1 and j == len(g[i])-1)

if __name__ == '__main__':
  print(solve(sys.stdin))
