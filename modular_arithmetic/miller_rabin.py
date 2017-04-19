import random
from pow_mod import powMod

def miller_rabin(n, k):
  if n == 2 or n == 3:
    return True

  if n % 2 == 0 or n < 2:
    return False

  s = 0
  d = n - 1

  while(d % 2 == 2):
    d  = d / 2
    s += 1

  a = random.randrange(2, n - 2, 1)
  x = powMod(a, d, n)

  if x == 1 or x == n - 1:
    return True

  i = 1
  while(i <= u - 1):
    x = powMod(a, 2, n)

    if a == p - 1:
      return True
    if a == 1:
      return False

    i += 1

  return False


