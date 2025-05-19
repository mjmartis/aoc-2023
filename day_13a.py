import sys

from day_13b import find_diff

def solve(instr):
  total = 0

  while True:
    g = []
    while l := instr.readline()[:-1]:
      g.append([c for c in l])
    
    if not g:
      break

    total += find_diff(g, 0) + 100 * find_diff(list(map(list, zip(*g))), 0)
  
  print(total)

if __name__ == '__main__':
  solve(sys.stdin)
