import sys

def parse_seqs(instream):
  return [list(map(int, l[:-1].split())) for l in instream.readlines()]

def extrap_poly(vs):
  if all(v == 0 for v in vs):
    return 0

  ds = [v - u for u, v in zip(vs, vs[1:])]
  return vs[-1] + extrap_poly(ds)

def solve(seqs):
  return sum(extrap_poly(ts) for ts in seqs)

if __name__ == '__main__':
  print(solve(parse_seqs(sys.stdin)))
