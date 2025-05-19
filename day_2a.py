import sys

LIMITS = {
  'red': 12,
  'green': 13,
  'blue': 14
}

def solve(instream):
  out = 0

  for line in instream.readlines():
    title, game = line[:-1].split(': ')
    game_num = int(title.split()[1])

    valid = True
    for draw in game.split('; '):
      for instance in draw.split(', '):
        count_str, colour = instance.split()
        count = int(count_str)
        if count > LIMITS[colour]:
          valid = False

    if valid:
      out += game_num

  print(out)

if __name__ == '__main__':
  solve(sys.stdin)
