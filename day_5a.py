from sys import stdin

from day_5b import parse_maps, solve

# I implemented 5b first, so retrofitting the solution for 5a.

def parse_seeds(instream):
  seed_tokens = [int(t) for t in instream.readline().strip().split()[1:]]
  seeds = sorted((s, s) for s in seed_tokens)
  instream.readline()
  return seeds

if __name__ == '__main__':
  solve(parse_seeds(stdin), *parse_maps(stdin))
