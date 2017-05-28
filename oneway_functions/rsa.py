import sys
sys.path.append('../modular_arithmetic')
from euclidean import extendedGcd
from pow_mod import powMod

p = 47257631 # 47257601
q = 19940131 # 19940125
n = 942323352889661 # p*q
euler = 942323285691900 # (p - 1) * (q - 1)

def calculate_e(euler):
    e = euler + 1
    while True:
        gcd = extendedGcd(e, euler)
        if gcd[0] == 1:
            break
        e += 1
    return e

def rsa(x):
    e = calculate_e(euler)
    result = powMod(x, e, n)
    print 'X, E, N: '
    print x, e, n

rsa(1234567890) # inverse ?
