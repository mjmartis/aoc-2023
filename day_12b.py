import sys

from day_12a import solve

def parse_input(instream):
  cases = []
  for l in instream.readlines():
    record_str, block_str = l[:-1].split()
    in_blocks = list(map(int, block_str.split(',')))
    cases.append(('?'.join([record_str] * 5), sum([in_blocks] * 5, [])))
  return cases

if __name__ == '__main__':
  print(solve(parse_input(sys.stdin)))
