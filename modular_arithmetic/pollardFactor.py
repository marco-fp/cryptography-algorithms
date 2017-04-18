from fractions import gcd

def pollardFactor(n):
    a = 2
    b = 2
    for i in xrange(1, n):
        a = (a*a + 1) % n
        b = (b*b + 1) % n
        b = (b*b + 1) % n
        d = gcd(p, q)
        if( 1 < d and d < n):
            return d
        if(d == n):
            return -1
