from stream_ciphers import golomb
from stream_ciphers import lfsr
from stream_ciphers import genGeffe


def main():

  trueGolomb = "100100011110101"
  falseGolomb = "01011100110110"

  print "Golomb for: " + trueGolomb + " is " + str(golomb.golomb(trueGolomb))
  print "Golomb for: " + falseGolomb + " is " + str(golomb.golomb(falseGolomb))

  pseudorand_binary_str = ''.join(map(str,lfsr.LFSR([1,0,1], [1,0,1], 10)))
  print "LFSR: " + pseudorand_binary_str
  print "Golomb: " + str(golomb.golomb(pseudorand_binary_str))

  message = "Don't Panic!"
  length = len(message)

  keystream = genGeffe.genGeffe([1,1,0,0,1,0], [1,1,1,1,0,1],
                       [1,0,1,0,1,1], [1,0,1,1,1,1],
                       [1,1,0,1,0,0], [1,1,0,1,0,0],
                       length)

  ciphered = genGeffe.encrypt_decrypt(keystream, message)

  print "Ciphered: " + str(ciphered)

  plain = genGeffe.encrypt_decrypt(keystream, ciphered)

  print "Plain text: " + str(plain)

  # Para conseguir p1p2p3 de periodo, los 3 deben ser primos relativos.
  print "For maximum period (p1p2p3): "
  keystreamMaxPeriod = genGeffe.genGeffe(
                        [1,0,1], [1,1,1],
                        [1,0,0,1], [1,1,1,1],
                        [1,0,0,1,0], [1,1,1,1,1], 100
                      )

  print keystreamMaxPeriod




if __name__ == '__main__':
    main()
