import sys

from day_6a import solve

def parse_input(instream):
  T = int(''.join(instream.readline()[:-1].split()[1:]))
  R = int(''.join(instream.readline()[:-1].split()[1:]))
  return [T], [R]

if __name__ == '__main__':
  print(solve(*parse_input(sys.stdin)))
