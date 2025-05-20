import sys
from queue import PriorityQueue

from utils import gv

def solve(instream):
  g = [[int(v) for v in l[:-1]] for l in instream.readlines()]

  costs = {}
  q = PriorityQueue()
  q.put((0, 0, 0, 0, 1, 10))
  q.put((0, 0, 0, 1, 0, 10))
  while not q.empty():
    cost, i, j, di, dj, rem_steps = q.get()

    if (i, j, di, dj, rem_steps) in costs:
      continue
    costs[(i, j, di, dj, rem_steps)] = cost

    dirs = [(di, dj, rem_steps-1)]
    if rem_steps <= 6:
      dirs.extend([(dj, di, 9), (-dj, -di, 9)])

    for (ndi, ndj, ns) in dirs:
      ni, nj = i + ndi, j + ndj
      if (dc := gv(g, ni, nj)) != None and (ni, nj, ndi, ndj, ns) not in costs and ns >= 0:
        q.put((cost + dc, ni, nj, ndi, ndj, ns))

  valid_exit = lambda i, j, n: i == len(g)-1 and j == len(g[0])-1 and n <= 6
  print(min(v for (i, j, _, _, n), v in costs.items() if valid_exit(i, j, n)))

if __name__ == '__main__':
  solve(sys.stdin)
