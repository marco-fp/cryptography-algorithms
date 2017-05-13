from lfsr import LFSR

def genGeffe(coef1, s1, coef2, s2, coef3, s3, length):
  c1 = LFSR(coef1, s1, length)
  c2 = LFSR(coef2, s2, length)
  c3 = LFSR(coef3, s3, length)

  res = []

  for i, j, k in zip(c1, c2, c3):
    x1 = i * j
    x2 = j * k
    x3 = k
    f = x1 ^ x2 ^ x3
    res.append(f)

  return res


def encrypt_decrypt(keystream, text):
  result = []
  for i, j in zip(text, keystream):
    result.append(chr(ord(i) ^ j))

  return result
