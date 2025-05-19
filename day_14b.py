import sys

from utils import gT, i_range

STEPS = 1000000000 * 4

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

def tilt_grid(g, d):
  for _ in range(d):
    g = rotate_cw(g)
  g = [tilt_row(r) for r in g]
  for _ in range((4-d) % 4):
    g = rotate_cw(g)
  return g

def calc_load(g):
  return sum(sum(i+1 for i, c in enumerate(r) if c == 'O') for r in g)

def solve(instream):
  g_in = [[c for c in l[:-1]] for l in instream.readlines()]

  # Iterate tilts until we see a repeat.
  have_seen_g = set()
  seen_gs = []
  g = rotate_cw(g_in)
  while True:
    g = tilt_grid(g, len(have_seen_g) % 4)
    if (key := tuple(map(tuple, g))) not in have_seen_g:
      have_seen_g.add(key)
      seen_gs.append(g)
    else:
      break
  
  # Find the start of the cycle and the offset into the cycle that matches the target
  # step.
  cycle_start_i = seen_gs.index(g)
  cycle_offset_i = (STEPS - 1 - cycle_start_i) % (len(seen_gs) - cycle_start_i)

  print(calc_load(seen_gs[cycle_start_i + cycle_offset_i]))

if __name__ == '__main__':
  solve(sys.stdin)
