from math import ceil
from isqrt import isqrt
from pow_mod import powMod
from inverse_mod import inverseMod

def babyStepGiantStep(alpha, beta, prime):
  """
    Returns log_alpha (beta) mod prime
  """

  m = int(ceil(isqrt(prime - 1)))

  Table = {}

  for j in xrange(m):
    alphaToJ = powMod(alpha, j, prime)
    Table[alphaToJ] = j

  alphaInverse = inverseMod(alpha, prime)
  alphaToMinusM = powMod(alphaInverse, m, prime)

  for i in xrange(m - 1):
    y = (beta * powMod(alphaToMinusM, i, prime)) % prime
    if Table.get(y) != None:
      return i*m + Table[y]
