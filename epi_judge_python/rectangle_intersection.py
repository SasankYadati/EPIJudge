import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    def is_intersect(r1: Rect, r2: Rect) -> bool:
        (x1, y1, w1, h1) = (r1.x, r1.y, r1.width, r1.height)
        (x2, y2, w2, h2) = (r2.x, r2.y, r2.width, r2.height)

        return (x1 <= x2 + w2 and x1 + w1 >= x2) and (y1 <= y2 + h2 and y1 + h1 >= y2)
    
    if is_intersect(r1, r2):
        x = max(r1.x, r2.x)
        width = min(r1.x + r1.width, r2.x + r2.width) - x
        y = max(r1.y, r2.y)
        height = min(r1.y + r1.height, r2.y + r2.height) - y
        return Rect(x, y, width, height)

    return Rect(0, 0, -1, -1)


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
