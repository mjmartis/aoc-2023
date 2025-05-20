import sys
from collections import defaultdict

SCORES = [
  'J',
  *[str(i) for i in range(2, 10)],
  'T', 'J', 'Q', 'K', 'A'
]

def solve(instream):
  data = []
  for l in instream.readlines():
    hand_str, bid_str = l[:-1].split()

    hand_mults = defaultdict(int)
    for c in [c for c in hand_str if c != 'J']:
      hand_mults[c] += 1

    if len(hand_mults) == 0:
      score = [5]
    else:
      score = sorted(hand_mults.values(), reverse=True)
      score[0] += hand_str.count('J')

    hand = tuple(SCORES.index(c) for c in hand_str)
    data.append((tuple(score), hand, int(bid_str)))

  print(sum((r+1) * b for r, (_, _, b) in enumerate(sorted(data))))

if __name__ == '__main__':
  solve(sys.stdin)
