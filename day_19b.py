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

def count_approvals(wfs, wf_name, r):
  if wf_name == 'A':
    return prod(u-l+1 for l, u in r.values())
  elif wf_name == 'R':
    return 0

  total = 0
  cur_rs = [r]
  for op, arg, lit, dest in wfs[wf_name][:-1]:
    next_rs = []
    for r in cur_rs:
      r_off, r_dir = (0, 1) if op == '<' else (1, -1)
      take, leave = cut_range(r, arg, lit+r_off)[::r_dir]

      if take:
        total += count_approvals(wfs, dest, take)
      if leave:
        next_rs.append(leave)

    cur_rs = next_rs

  uncond_dest = wfs[wf_name][-1][-1]
  total += sum(count_approvals(wfs, uncond_dest, r) for r in cur_rs)
  return total

def solve(instream):
  wfs = parse_wfs(instream)
  return count_approvals(wfs, 'in', {p: (1, MAX_COORD) for p in 'xmas'})

if __name__ == '__main__':
  print(solve(sys.stdin))
