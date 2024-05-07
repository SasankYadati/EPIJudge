from test_framework import generic_test

MASK_SIZE = 16
PRECOMPUTED_REVERSE = {}

def reverse(x:int) -> int:
    x_rev = 0
    for _ in range(16):
        x_rev = x_rev << 1
        b = x & 1
        x_rev = x_rev ^ b
        x = x >> 1
    return x_rev

def precomputeReverse():
    for i in range(0, 2**MASK_SIZE):
        PRECOMPUTED_REVERSE[i] = reverse(i)

def reverse_bits(x: int) -> int:
    # TODO - you fill in here.
    mask = 2**MASK_SIZE-1
    x1 = x & mask
    x2 = (x >> MASK_SIZE) & mask
    x3 = (x >> (2*MASK_SIZE)) & mask
    x4 = (x >> (3*MASK_SIZE)) & mask

    return ((PRECOMPUTED_REVERSE[x1] << (3*MASK_SIZE)) 
            ^ (PRECOMPUTED_REVERSE[x2] << (2*MASK_SIZE))
            ^ (PRECOMPUTED_REVERSE[x3] << (MASK_SIZE))
            ^ (PRECOMPUTED_REVERSE[x4]))



if __name__ == '__main__':
    precomputeReverse()
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
