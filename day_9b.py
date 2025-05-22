import sys

from day_9a import parse_seqs, solve

if __name__ == '__main__':
  print(solve([s[::-1] for s in parse_seqs(sys.stdin)]))
