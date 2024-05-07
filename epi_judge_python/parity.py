from test_framework import generic_test


PRECOMPUTED_PARITY = {}

def parity_naive(x: int) -> int:
    # TODO - you fill in here.
    result = 0
    while x:
        result ^= 1
        x = x & (x-1) # reset the lowest set bit
    return result

def parity_cache(x: int) -> int:
    mask_size = 16
    bit_mask = (2**16)-1
    return (PRECOMPUTED_PARITY[x >> (3 * mask_size)] ^
            (PRECOMPUTED_PARITY[x >> (2 * mask_size) & bit_mask]) ^
            (PRECOMPUTED_PARITY[x >> (mask_size) & bit_mask]) ^
            (PRECOMPUTED_PARITY[x & bit_mask]))

def parity(x: int) -> int:
    x = x ^ (x >> 32)
    x = x ^ (x >> 16)
    x = x ^ (x >> 8)
    x = x ^ (x >> 4)
    x = x ^ (x >> 2)
    x = x ^ (x >> 1)
    return x & 1

def precompute_parity():
    for i in range(2**16):
        PRECOMPUTED_PARITY[i] = parity_naive(i)

if __name__ == '__main__':
    # precompute_parity()
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
