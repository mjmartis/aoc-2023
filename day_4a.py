import sys

def solve(instream):
  total = 0
  for l in instream.readlines():
    ts = l[:-1].split()
    mid = ts.index('|')
    winners = set(map(int, ts[2:mid]))
    mine = set(map(int, ts[mid+1:]))
    matches = len(winners & mine)
    if matches > 0:
      total += 2 ** (matches - 1)
  print(total)

if __name__ == '__main__':
  solve(sys.stdin)
