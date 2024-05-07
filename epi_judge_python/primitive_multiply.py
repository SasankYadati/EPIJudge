from test_framework import generic_test

def add(x: int, y: int) -> int:
    if y == 0:
        return x
    return add(x ^ y, (x & y) << 1)

def multiply(x: int, y: int) -> int:
    if x == 0 or y == 0:
        return 0
    if x & 1:
        return add(multiply(x >> 1, y << 1), y)
    else:
        return multiply(x >> 1, y << 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
