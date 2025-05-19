import sys

def solve(instream):
  total = 0
  for l in instream.readlines():
    vs = [c for c in l if c.isnumeric()]
    total += int(vs[0] + vs[-1])
  print(total)

if __name__ == '__main__':
  solve(sys.stdin)
