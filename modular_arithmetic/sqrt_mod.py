from jacobi import jacobi
from pow_mod import powMod

def sqrtMod(a, p):
  if(p%4 == 3):
    m = (p - 3) / 4
    return powMod(a, m + 1, p)

  if(p%4 == 1):
    b = lookForB(p)
    i = m*2
    j = 0

    while(i%2 == 0):
      i /= 2
      j /= 2

      if((powMod(a,i,p) * powMod(b,j,p))%p == p - 1 ):
        j = (j+(m*2)) % p

    return (powMod(a, (i+1)/2, p) * powMod(b, j/2, p)) % p


def lookForB(p):
  for b in xrange(p):
    if(jacobi(b, p) == -1):
      return b
