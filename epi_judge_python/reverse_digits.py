from test_framework import generic_test


def reverse(x: int) -> int:
    rev = 0
    sign_multiplier = -1 if x < 0 else 1
    x = sign_multiplier * x
    while x:
        rev = rev * 10 + (x % 10)
        x = x // 10
    rev = sign_multiplier * rev
    return rev


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
