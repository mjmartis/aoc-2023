import sys
from functools import reduce
from collections import OrderedDict
import re

def hash(s):
  return reduce(lambda acc, c: (acc + ord(c)) * 17 % 256, s, 0)

def solve(instream):
  tokens = ''.join(l[:-1] for l in instream.readlines()).split(',')
  boxes = [OrderedDict() for _ in range(256)]
  for token in tokens:
    label, lens = re.match(r'([a-z]+)(?:=(\d+)|-)', token).groups()  # pyright: ignore
    box = hash(label)

    if lens is not None:
      boxes[box][label] = int(lens)
    elif label in boxes[box]:
      del boxes[box][label]

  power = lambda i, b: sum((i+1) * (j+1) * f for j, (_, f) in enumerate(b.items()))
  return sum(power(i, b) for i, b in enumerate(boxes))

if __name__ == '__main__':
  print(solve(sys.stdin))
