import sys
from collections import defaultdict
from math import prod

def solve(instream):
  out = 0

  for line in instream.readlines():
    _, game = line[:-1].split(': ')

    mins = defaultdict(int)
    for draw in game.split('; '):
      for instance in draw.split(', '):
        count_str, colour = instance.split()
        count = int(count_str)
        mins[colour] = max(mins[colour], count)

    out += prod(mins.values())

  return out

if __name__ == '__main__':
  print(solve(sys.stdin))
