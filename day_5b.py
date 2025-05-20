from sys import stdin
import re

def parse_seeds(instream):
  seed_tokens = [int(t) for t in instream.readline().strip().split()[1:]]
  seed_lens = zip(seed_tokens[::2], seed_tokens[1::2])
  seeds = sorted((s, s+l-1) for s, l in seed_lens)
  instream.readline()
  return seeds

def parse_maps(instream):
  next_map = {}
  maps = {}
  while (title_line := instream.readline()) != '':
    # Read which map we're populating.
    src_map, _, dest_map = re.split(r'\W+', title_line)[:3]
    next_map[src_map] = dest_map
    maps[src_map] = []

    # Read contents of map.
    while (line := instream.readline()[:-1]) != '':
      maps[src_map].append(tuple(int(t) for t in line.split()))
    maps[src_map].sort(key=lambda v: v[1])

  return next_map, maps

def apply_maps(spans, maps):
  # Maps and spans must be sorted by starting ID.
  mapped = []

  map_i = 0
  span_i = 0
  unmapped_start = spans[0][0]

  while span_i < len(spans):
    span_start, span_end = spans[span_i]
    unmapped_start = max(unmapped_start, span_start)

    # Iterate through maps that are too early.
    map_dest, map_src, map_width = None, None, None
    while map_i < len(maps):
      map_dest, map_src, map_width = maps[map_i]
      if map_src + map_width > unmapped_start:
        break
      map_i += 1

    # We use the identity map if we're out of other maps or if we are at an "non-covered"
    # section of the current span. Otherwise, we use the subset of the map that covers
    # the current span.
    end, offset = None, None
    if map_i < len(maps) and unmapped_start < map_src:
      assert map_src is not None
      end = min(map_src - 1, span_end)
      offset = 0
    elif map_i == len(maps):
      end = span_end
      offset = 0
    else:
      assert map_src is not None and map_dest is not None
      end = min(span_end, map_src + map_width - 1)
      offset = map_dest - map_src

    mapped.append((unmapped_start + offset, end + offset))

    unmapped_start = end + 1
    if unmapped_start > span_end:
      span_i += 1

    # Would have to dedup if mapping wasn't injective.

  return sorted(mapped)

def solve(seeds, next_map, maps):
  cur_type = 'seed'
  cur_spans = seeds
  while cur_type in maps:
    cur_spans = apply_maps(cur_spans, maps[cur_type])
    cur_type = next_map.get(cur_type, None)

  print(min(v for v, _ in cur_spans))

if __name__ == '__main__':
  solve(parse_seeds(stdin), *parse_maps(stdin))
