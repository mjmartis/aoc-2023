import sys
import re

def solve(instream):
  ins = instream.readline()[:-1]
  instream.readline()

  nexts = {}
  for line in instream.readlines():
    v, l, r = re.match(r'(\w+)\s*=\s*\((\w+),\s*(\w+)\)', line[:-1]).groups()  # pyright: ignore
    nexts[v] = (l, r)

  i = 0
  cur = 'AAA'
  while cur != 'ZZZ':
    cur = nexts[cur][0 if ins[i % len(ins)] == 'L' else 1]
    i += 1

  print(i)

if __name__ == '__main__':
  solve(sys.stdin)
