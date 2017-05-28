import random
import binascii

n = 48478872564493742276963
a0 = random.getrandbits(10)**2 % n
a1 = random.getrandbits(10)**2 % n

def to_binary(str):
    return bin(int(binascii.hexlify(message), 16))[2:]

def h(b, x):
    return (x**2 * a0**b * a1**(1-b)) % n

def merkle_damgard(message, seed):
    hash_result = seed
    for i in xrange(len(message)):
        hash_result = h(int(message[i]), hash_result)

    return hash_result

message = 'Cryptography is the ultimate form of non-violent direct action.'
print 'Message: '
print message
print 'Hash: '
print merkle_damgard(to_binary(message), 1337)
