import fractions
import random
import sys
sys.path.append('../modular_arithmetic')
from miller_rabin import miller_rabin
from pow_mod import powMod
from baby_step_giant_step import babyStepGiantStep

def next_prime(p):
    next_p = p + 1
    while not miller_rabin(next_p) or not miller_rabin((next_p-1)/2):
        next_p += 1

    return next_p

def get_generator(p):
    a = random.randint(2, p - 1)
    while powMod(a, (p - 1)/2, p) == 1: # ??
        a = random.randint(2, p - 1)
    return a

p = next_prime(47257601)
a = get_generator(p)
birth_number = 19940125
inverse_birth_number = babyStepGiantStep(a, birth_number, p)

print 'Prime is: '
print p
print 'a is: '
print a
print 'Birth-number is: '
print birth_number
print 'log_a(birth-number) mod p = inverse_birth_number mod p'
print 'Inverse Birth-number mod p: '
print inverse_birth_number
