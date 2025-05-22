import sys
from collections import defaultdict

SCORES = [
  *[str(i) for i in range(2, 10)],
  'T', 'J', 'Q', 'K', 'A'
]

def solve(instream):
  data = []
  for l in instream.readlines():
    hand_str, bid_str = l[:-1].split()

    hand_mults = defaultdict(int)
    for c in hand_str:
      hand_mults[c] += 1
    score = tuple(sorted(hand_mults.values(), reverse=True))

    hand = tuple(SCORES.index(c) for c in hand_str)
    data.append((score, hand, int(bid_str)))

  return sum((r+1) * b for r, (_, _, b) in enumerate(sorted(data)))

if __name__ == '__main__':
  print(solve(sys.stdin))
