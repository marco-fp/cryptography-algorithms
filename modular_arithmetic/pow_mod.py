def powMod(base, exp, mod):
  """
    Returns base to the power of exp modulus mod.
  """
  result = 1
  if k == 0:
      return result
  A = base
  if 1 & exp: # Last bit of exp is 1 => is pair.
      result = base

  exp = exp >> 1

  while exp:
      A = (A**2) % mod
      if 1 & exp:
          result = (result * A) % mod
      exp = exp >> 1

  return result
