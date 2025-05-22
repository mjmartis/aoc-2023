import sys
import re
from math import gcd
from functools import reduce

def lcm(a, b):
  return abs(a * b) // gcd(a, b)

def count_cycle_len(ins, nexts, cur):
  i = 0
  while cur[-1] != 'Z':
    cur = nexts[cur][0 if ins[i % len(ins)] == 'L' else 1]
    i += 1
  return i

def solve(instream):
  ins = instream.readline()[:-1]
  instream.readline()

  nexts = {}
  for line in instream.readlines():
    v, l, r = re.match(r'(\w+)\s*=\s*\((\w+),\s*(\w+)\)', line[:-1]).groups()  # pyright: ignore
    nexts[v] = (l, r)

  lens = [count_cycle_len(ins, nexts, s) for s in nexts if s[-1] == 'A']
  return reduce(lcm, lens)

if __name__ == '__main__':
  print(solve(sys.stdin))
