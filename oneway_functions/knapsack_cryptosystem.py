import sys
sys.path.append('../modular_arithmetic')
from inverse_mod import inverseMod
# Following:
# https://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem
# Using private key parameters as shown in example.

q = 881
w = 706
r = 588
sup_inc_sec = [2, 7, 11, 21, 42, 89, 180, 354]

def encrypt(m, sequence):
    public_key = []
    for i in xrange(len(sequence)):
        public_key.append((sequence[i] * r) % q)

    ciphertext = 0
    for i in xrange(len(sequence)):
        ciphertext += m[i] * public_key[i]

    return ciphertext

def decrypt(c, sequence):
    s = (inverseMod(r, q) * c) % q
    plaintext = []

    i = len(sequence) - 1

    while s != 0:
        if s >= sequence[i]:
            s -= sequence[i]
            plaintext.append(1)
        else:
            plaintext.append(0)

        i -= 1

    plaintext.reverse()
    return plaintext

# Both tobits taken from 'Simon Streicher':
# https://stackoverflow.com/questions/10237926/convert-string-to-list-of-bits-and-viceversa
def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

message = "A"
ciphered = encrypt(tobits(message), sup_inc_sec)
deciphered = decrypt(ciphered, sup_inc_sec)

print 'Message: '
print message
print tobits(message)
print 'Ciphered: '
print ciphered
print 'Deciphered: '
print chr(int(''.join(map(str, deciphered)),2))
