from euclidean import extendedGcd

def inverseMod(a, n):
  """
    Inverse of a mod n
  """

  d, x, y = extendedGcd(a, n)

  if d > 1:
    return "Inverse doesnt exist."
  else:
    return x % n
