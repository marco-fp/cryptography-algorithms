def berlekampMassey(s):
  C = [1]
  L = 0
  m = -1
  B = [1]
  N = 0
  T = []

  n = len(s)

  while(N < n):
    discrepancy = s[N]
    discrepancy_sum = 0
    for i in xrange(1, L): # L is 0 at start, must iterate once.
      discrepancy_sum = c[i]*s[N-i]

    discrepancy += discrepancy_sum
    discrepancy = discrepancy % 2

    if d == 1:

