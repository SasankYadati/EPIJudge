from test_framework import generic_test


def power(x: float, y: int) -> float:
    if y == 0:
        return 1
    else:
        if y < 0:
            x = 1/x
            y = -y
        p = power(x, (y >> 1))
        if y & 1:
            return (p * p) * x
        else:
            return (p * p)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
