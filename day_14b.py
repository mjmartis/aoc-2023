import sys

from utils import gT, i_range

CYCLES = 1000000000

def rotate_cw(g):
  return [c[::-1] for c in gT(g)]

def tilt_row(row):
  tilted = []
  rock_count = 0
  for i in i_range(row, o=1):
    if i == len(row) or row[i] == '#':
      tilted += ['.'] * (i - len(tilted) - rock_count)
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
  have_seen_g = set()
  seen_gs = []
  g = rotate_cw(g_in)
  while True:
    # Complete a full cycle before caching.
    #
    # If the number of unique board states is coprime with 4, this would require 4x more
    # iterations than caching a tilt at a time. However for my problem input, caching by
    # cycles proves faster.
    for _ in range(4):
      g = rotate_cw([tilt_row(r) for r in g])

    if (key := tuple(map(tuple, g))) not in have_seen_g:
      have_seen_g.add(key)
      seen_gs.append(g)
    else:
      break
  
  # Find the start of the loop and offset into the loop that matches the target step.
  loop_start_i = seen_gs.index(g)
  loop_offset_i = (CYCLES-1-loop_start_i) % (len(seen_gs)-loop_start_i)

  print(calc_load(seen_gs[loop_start_i+loop_offset_i]))

if __name__ == '__main__':
  solve(sys.stdin)
