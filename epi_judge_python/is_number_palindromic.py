from test_framework import generic_test


def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    
    def n_digits(x):
        n = 0
        while x:
            n += 1
            x //= 10
        return n
    
    n = n_digits(x)
    while n > 1:
        last_digit = x % 10
        first_digit = x // (10 ** (n-1))
        if last_digit != first_digit:
            return False
        x = x % (10 ** (n - 1)) # remove first digit
        x = x // 10 # remove last digit
        n -= 2
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
