import sys

from utils import i_range

def parse_input(instream):
  cases = []
  for l in instream.readlines():
    record, block_str = l[:-1].split()
    blocks = list(map(int, block_str.split(',')))
    cases.append((record, blocks))
  return cases

def solve(cases):
  total = 0

  for record, blocks in cases:
    record = record + '.'

    # How many ways can we place the first n blocks followed by one or more spaces before
    # index i?
    init_ways = [0 if '#' in record[:i] else 1 for i in i_range(record, o=1)]
    ways = [init_ways] + [[0] * (len(record)+1) for _ in i_range(blocks)]

    for i in range(1, len(blocks)+1):
      for j in range(blocks[i-1]+1, len(record)+1):
        # Could append a space to any previous solution, or place the block and one space
        # at this position if that's valid.

        if record[j-1] == '#':
          continue
        
        ways[i][j] = ways[i][j-1]
        if '.' not in record[j-blocks[i-1]-1:j-1]:
          ways[i][j] += ways[i-1][j-blocks[i-1]-1]

    total += ways[len(blocks)][len(record)]

  print(total)

if __name__ == '__main__':
  solve(parse_input(sys.stdin))
