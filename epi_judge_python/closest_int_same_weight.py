from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    n_bits = 64
    for i in range(n_bits-1):
        b1 = (x >> i) & 1
        b2 = (x >> (i+1)) & 1
        if b1 != b2:
            x = x ^ (1 << i)
            x = x ^ (1 << (i + 1))
            return x
    
    raise ValueError("x is all zeros or ones")
            


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
