import sys

from utils import gT, i_range

CYCLES = 1000000000

def rotate_cw(g):
  return [c[::-1] for c in gT(g)]

def tilt_row(row):
  tilted = []
  rock_count = 0
  for i in i_range(row, buf=1):
    if i == len(row) or row[i] == '#':
      tilted += ['.'] * (i-len(tilted)-rock_count)
      tilted += ['O'] * rock_count + row[i:i+1]
      rock_count = 0
    elif row[i] == 'O':
      rock_count += 1
  return tilted

def calc_load(g):
  return sum(sum(i+1 for i, c in enumerate(r) if c == 'O') for r in g)

def solve(instream):
  g_in = [[c for c in l[:-1]] for l in instream.readlines()]

  # Iterate cycles until we see a repeat.
  seen_gs = set()
  gs = []
  g = rotate_cw(g_in)
  while True:
    # Complete a full cycle before caching.
    #
    # If the number of unique board states is coprime with 4, this would require 4x more
    # iterations than caching a tilt at a time. However for my problem input, caching by
    # cycles proves faster.
    for _ in range(4):
      g = rotate_cw([tilt_row(r) for r in g])

    if (key := tuple(map(tuple, g))) not in seen_gs:
      seen_gs.add(key)
      gs.append(g)
    else:
      break
  
  # Find the start of the loop and offset into the loop that matches the target step.
  loop_start_i = gs.index(g)
  loop_offset_i = (CYCLES-1-loop_start_i) % (len(gs)-loop_start_i)

  print(calc_load(gs[loop_start_i+loop_offset_i]))

if __name__ == '__main__':
  solve(sys.stdin)
