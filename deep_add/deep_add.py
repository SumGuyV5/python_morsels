from collections.abc import Iterable
from datetime import timedelta


def deep_add(lst, start=0):
    if isinstance(lst, Iterable):
        for x in lst:
            start = deep_add(x, start)
        return start
    return lst + start


if __name__ == '__main__':
    print(f'{deep_add([[timedelta(5), timedelta(10)], [timedelta(3)]], start=timedelta(0))}')

