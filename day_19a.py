import sys
from collections import defaultdict
import re

def apply_wfs(q, wfs):
  cur_wf = 'in'
  while cur_wf not in ['A', 'R']:
    for op, arg, lit, dest in wfs[cur_wf]:
      sign = -1 if not op or op == '<' else 1
      if not op or lit * sign < q[arg] * sign:
        cur_wf = dest
        break

  return cur_wf

def parse_wfs(instream):
  wfs = defaultdict(list)
  while (l := instream.readline()[:-1]) != '':
    name, preds = re.match(r'(\w+)\{(.*?)\}', l).groups()  # pyright: ignore

    for pred in preds.split(','):
      if (m := re.match(r'(\w+)([<>])(\d+):(\w+)', pred)):
        wfs[name].append((m.group(2), m.group(1), int(m.group(3)), m.group(4)))
      else:
        wfs[name].append((None, None, None, pred))

  return wfs

def solve(instream):
  wfs = parse_wfs(instream)

  queries = []
  while (l := instream.readline()[:-1]) != '':
    queries.append({})
    for match in re.finditer(r'(\w+)=(\d+)', l):
      param, val = match.groups()
      queries[-1][param] = int(val)
  
  total = 0
  for q in queries:
    cur_wf = 'in'
    while cur_wf not in ['A', 'R']:
      for op, arg, lit, cond in wfs[cur_wf]:
        sign = -1 if not op or op == '<' else 1
        if not op or lit * sign < q[arg] * sign:
          cur_wf = cond
          break

    if cur_wf == 'A':
      total += sum(q.values())

  return total

if __name__ == '__main__':
  print(solve(sys.stdin))
