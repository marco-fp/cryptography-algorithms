"""
  Marco Fernandez Pranno
  Ejercicio 1
"""

def extendedGcd(a, b):
  """
  Greatest common divisor d of a and b, and x and y integers satisfying ax + by = d
  """
  if b == 0:
    return a, 1, 0

  x1 = 0
  x2 = 1
  y1 = 1
  y2 = 0

  while b != 0:
    q = a // b
    r = a - q * b
    x = x2 - q * x1
    y = y2 - q  * y1

    a = b
    b = r
    x2 = x1
    x1 = x
    y2 = y1
    y1 = y

if a < 0:
  return -a. -x2, -y2

return a, x2, y2
