import sys

def solve(instream):
  total = 0
  for s in ''.join(l[:-1] for l in instream.readlines()).split(','):
    case_total = 0
    for c in s:
      case_total = (case_total + ord(c)) * 17 % 256
    total += case_total
  return total

if __name__ == '__main__':
  print(solve(sys.stdin))
