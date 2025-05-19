import sys
from collections import defaultdict

def solve(instream):
  copies = defaultdict(lambda: 1)

  for i, l in enumerate(instream.readlines()):
    copies[i]

    ts = l[:-1].split()
    mid = ts.index('|')
    winners = set(map(int, ts[2:mid]))
    mine = set(map(int, ts[mid+1:]))

    for j in range(i+1, i+len(winners & mine)+1):
      copies[j] += copies[i]

  print(sum(copies.values()))

if __name__ == '__main__':
  solve(sys.stdin)
