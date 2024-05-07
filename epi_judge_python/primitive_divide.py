from test_framework import generic_test


def divide(x: int, y: int) -> int:
    if x < y:
        return 0
    largest_k = 0
    while (y << (largest_k+1)) <= x:
        largest_k += 1
    return divide(x - (y << largest_k), y) + (1 << largest_k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
