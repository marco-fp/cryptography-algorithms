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


message = "Don't Panic!"
length = len(message)

keystream = genGeffe([1,1,0,0,1,0], [1,1,1,1,0,1],
                     [1,0,1,0,1,1], [1,0,1,1,1,1],
                     [1,1,0,1,0,0], [1,1,0,1,0,0],
                     length)

ciphered = encrypt_decrypt(keystream, message)

print "Ciphered: " + str(ciphered)

plain = encrypt_decrypt(keystream, ciphered)

print "Plain text: " + str(plain)

# Para conseguir p1p2p3 de periodo, los 3 deben ser primos relativos.
