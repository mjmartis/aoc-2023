''' Helper functions. '''

def gT(m):
  ''' Transpose a grid. '''
  return list(map(list, zip(*m)))

def gv(g, i, j):
  ''' Guarded lookup of a location in a grid. '''
  if 0 <= i < len(g) and 0 <= j < len(g[0]):
    return g[i][j]
  return None

def i_range(v, buf=0):
  ''' Range of the indices of a collection. '''
  return range(len(v)+buf)