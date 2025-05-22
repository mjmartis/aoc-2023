import sys

from utils import gT

def calc_load(row, i, rock_count, load_acc):
  if i > len(row):
    return load_acc

  if i == len(row) or row[i] == '#':
    # Closed form for `i + (i - 1) + ...` with rock_count terms.
    load = rock_count * (2*i - rock_count + 1) // 2
    return calc_load(row, i+1, 0, load_acc+load)

  return calc_load(row, i+1, rock_count + (1 if row[i] == 'O' else 0), load_acc)

def solve(instream):
  g = [[c for c in l[:-1]] for l in instream.readlines()]
  rows = [c[::-1] for c in gT(g)]  # Rotated clockwise 90 degrees.

  return sum([calc_load(row, 0, 0, 0) for row in rows])

if __name__ == '__main__':
  print(solve(sys.stdin))
