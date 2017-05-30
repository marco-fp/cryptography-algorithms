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

    output_file = open("rsa_key.priv", "w")
    output_file.write(str(d) + '\n ' + str(n))
    output_file.close()

    output_file = open("rsa_key.pub", "w")
    output_file.write(str(e) + '\n ' + str(n))
    output_file.close()

    return ('rsa_key.pub', 'rsa_key.priv')


def sign(privKey_filename, message_filename):
    privKey = tuple(open(privKey_filename, 'r'))
    key, n = privKey

    message_file = tuple(open(message_filename, 'r'))
    message = message_file[0]

    hashedMessage = int(sha512(message).hexdigest(), 16)
    signature = powMod(hashedMessage, int(key), int(n))

    signature_filename = 'rsa_signature'
    output_file = open(signature_filename, "w")
    output_file.write(str(signature))
    output_file.close()

    return signature_filename


def verify(pubKey_filename, message_filename, signature_filename):
    pubKey = tuple(open(pubKey_filename, 'r'))
    key, n = pubKey

    message_file = tuple(open(message_filename, 'r'))
    message = message_file[0]

    signature_file = tuple(open(signature_filename, 'r'))
    signature = signature_file[0]

    hashedMessage = int(sha512(message).hexdigest(), 16) % int(n)
    plainSignature = powMod(int(signature), int(key), int(n))

    return plainSignature == hashedMessage


def main_test():
    message = "Hello my name is Marco"
    message_filename = 'message.txt'

    print 'Message: ', message
    print 'Writing message to file: \'%s\'' % message_filename

    output_file = open(message_filename, "w")
    output_file.write(str(message))
    output_file.close()

    print 'Generating keys, saving them into files: \'rsa_key.priv\' - \'rsa_key.pub\''
    pub_filename, priv_filename = generate_keys(prime1, prime2)

    print 'Public key filename: ', pub_filename
    print 'Private key filename: ', priv_filename

    signature_filename = sign(priv_filename, message_filename)

    print 'Signature filename: ', signature_filename

    result = verify(pub_filename, message_filename, signature_filename)

    print result
    

main_test()
