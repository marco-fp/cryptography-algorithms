from isqrt import isqrt
from math import ceil

def fermatFactor(n):
  a = int(ceil(isqrt(n)))
  b2 = a*a - n
  b = int(ceil(isqrt(b2)))

  while(b*b != b2):
    a += 1
    b2 = a*a - n
    b = int(ceil(isqrt(b2)))

  factorA = a + b
  factorB = a - b

  return factorA, factorB
