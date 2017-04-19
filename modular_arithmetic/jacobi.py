def jacobi(a,n):
  if a == 0:
      return 0
  if a == 1:
      return 1

  a1 = a
  e = 0

  while a1%2 == 0:
      e += 1
      a1 /= 2

  if e%2 == 0:
      s = 1
  else:
      if n%8 == 1 or n%8 == 7:
          s = 1
      if n%8 == 3 or n%8 == 5:
          s = -1

  if n%4 == 3 and a1%4 == 3:
      s = -s
  n1 = n%a1
  if a1 == 1:
      return s
  else:
      return s * jacobi(n1,a1)
