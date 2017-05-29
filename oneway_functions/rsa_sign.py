import hashlib
from hashlib import sha512
import random
import sys
sys.path.append('../modular_arithmetic')
from inverse_mod import inverseMod
from euclidean import gcd
from pow_mod import powMod

# Based on:
# https://en.wikipedia.org/wiki/Digital_signature

sha1Hash = hashlib.sha512()

prime1 = 47257631
prime2 = 19940131

def generate_keys(p, q):
    n = p * q
    phiEuler = (p-1) * (q-1)
    e = random.randint(1, phiEuler)


    while gcd(e, phiEuler) != 1:
        e = random.randint(1, phiEuler)

    d = inverseMod(e, phiEuler)

    pubKey = (e, n)
    privKey = (d, n)
    return (pubKey, privKey)

def sign(privKey, message):
    key, n = privKey
    hashedMessage = int(sha512(message).hexdigest(), 16)
    signature = powMod(hashedMessage, key, n)

    return signature

def verify(pubKey, message, signature):
    key, n = pubKey
    hashedMessage = int(sha512(message).hexdigest(), 16) % n
    plainSignature = powMod(signature, key, n)

    return plainSignature == hashedMessage



msg = "Hello my name is Marco"
publicKey, privateKey = generate_keys(prime1, prime2)
print 'pubkey: ', publicKey
print 'privkey: ', privateKey
signature = sign(privateKey, msg)
print 'signature: ', signature
result = verify(publicKey, msg, signature)

print result
