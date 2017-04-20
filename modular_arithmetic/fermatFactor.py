from isqrt import isqrt
from math import ceil

def fermatFactor(n):
  a = isqrt(n)
  b2 = a*a - n
  b = isqrt(n)

  while(b*b != b2):
    a += 1
    b2 = a*a - n
    b = isqrt(b2)

  factorA = a + b
  factorB = a - b

  return factorA, factorB
