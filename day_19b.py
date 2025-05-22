import sys
from math import prod

MAX_COORD = 4000

from day_19a import parse_wfs

def cut_range(r, coord, cut):
  low, high = r[coord]

  if low > cut:
    return (None, r)
  
  if high < cut:
    return (r, None)

  return {**r, coord: (low, cut-1)}, {**r, coord: (cut, high)}

def count_approvals(wfs, wf_name, params):
  if wf_name == 'A':
    return prod(u-l+1 for l, u in params.values())
  elif wf_name == 'R':
    return 0

  total = 0
  cur_params = [params]
  for op, var, val, dest in wfs[wf_name][:-1]:
    next_params = []
    for p in cur_params:
      cmp = 0 if op == '<' else -1
      take, leave = cut_range(p, var, val-cmp)[::(cmp or 1)]

      if take:
        total += count_approvals(wfs, dest, take)
      if leave:
        next_params.append(leave)

    cur_params = next_params

  uncond_dest = wfs[wf_name][-1][-1]
  total += sum(count_approvals(wfs, uncond_dest, p) for p in cur_params)
  return total

def solve(instream):
  wfs = parse_wfs(instream)

  total = count_approvals(wfs, 'in', {
    'x': (1, MAX_COORD),
    'm': (1, MAX_COORD),
    'a': (1, MAX_COORD),
    's': (1, MAX_COORD),
  })

  print(total)

if __name__ == '__main__':
  solve(sys.stdin)
