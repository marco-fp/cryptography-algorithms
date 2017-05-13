'''
 Lecture on Strem Ciphers and LFSR by Christopf Paar (https://www.youtube.com/watch?v=sKUhFpVxNWc)
 Handbook of Applied Cryptography, chapter 6.
'''

from golomb import golomb

def LFSR(polynomial, seed, output_length):
    '''
        INPUT:
            - polynomial: Connection polynomial given as an array of 1s and 0s.
            - seed: Initial values of the flipflops of the LFSR.
            - output_length: Number of values to output.

        OUTPUT: Pseudorandom stream of s values, where s = {0,1}.
    '''

    if(len(polynomial) != len(seed)):
        return None

    output = []
    flipflops = seed

    for j in xrange(output_length):
        s = 0
        for i in xrange(len(polynomial)): # Same as polynomial length, expected to be array of 0's and 1's.
            c = flipflops[i] & polynomial[i]
            s = s ^ c

        output.append(flipflops[len(flipflops) - 1])
        flipflops = [s] + flipflops[:-1] # Add feedback to as first element and pop last element (output-ed).

    return output


# pseudorand_binary_str = ''.join(map(str,LFSR([1,0,0,1], [1,0,0,1], 2**4 - 1)))
# print pseudorand_binary_str
# print golomb(pseudorand_binary_str)
