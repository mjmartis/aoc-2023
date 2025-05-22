import sys
from math import sqrt, ceil, floor

EPS = 1e-6

def parse_input(instream):
  Ts = list(map(int, instream.readline()[:-1].split()[1:]))
  Rs = list(map(int, instream.readline()[:-1].split()[1:]))
  return Ts, Rs

def solve(Ts, Rs):
  total = 1

  for T, R in zip(Ts, Rs):
    t1 = -(-T - sqrt(T ** 2 - 4 * R)) / 2
    t2 = -(-T + sqrt(T ** 2 - 4 * R)) / 2
    if t1 > t2:
      t1, t2 = t2, t1

    ways_count = max(floor(t2 - EPS) - ceil(t1 + EPS) + 1, 0)
    total *= ways_count

  return total

if __name__ == '__main__':
  print(solve(*parse_input(sys.stdin)))
