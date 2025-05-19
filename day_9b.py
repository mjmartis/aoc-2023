import sys

def extrap_poly(vs):
  if all(v == 0 for v in vs):
    return 0

  ds = [v - u for u, v in zip(vs, vs[1:])]
  return vs[0] - extrap_poly(ds)

def solve(instream):
  total = 0
  for l in instream.readlines():
    ts = list(map(int, l[:-1].split()))
    total += extrap_poly(ts)
  print(total)

if __name__ == '__main__':
  solve(sys.stdin)
