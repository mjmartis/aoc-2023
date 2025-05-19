import sys

from utils import i_range

RS = [
  'one',
  'two',
  'three',
  'four',
  'five',
  'six',
  'seven',
  'eight',
  'nine',
]

RSIS = dict([(v, i + 1) for i, v in enumerate(RS)])

def find_num(s, d):
  for i in i_range(s)[::d]:
    if s[i].isnumeric():
      return int(s[i])

    for c, n in RSIS.items():
      if s[i:].startswith(c):
        return n

  return -1

def solve(instream):
  total = 0
  for l in instream.readlines():
    total += 10 * find_num(l, 1) + find_num(l, -1)
  print(total)

if __name__ == '__main__':
  solve(sys.stdin)
