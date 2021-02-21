from itertools import chain
from collections.abc import Iterable


def list_flatten(num):
    return list(chain.from_iterable(num))


def tuple_flatten(test_tuple):
    if isinstance(test_tuple, tuple) and len(test_tuple) == 2 and not isinstance(test_tuple[0], tuple):
        res = [test_tuple]
        return res

    res = []
    for sub in test_tuple:
        res += tuple_flatten(sub)
    return res


def deep_flattenold(nums):
    flattened = []
    for item in nums:
        if isinstance(item, Iterable):
            flattened.extend(deep_flatten(item))
        else:
            flattened.append(item)
    return flattened


def deep_flatten(nums):
    for item in nums:
        if isinstance(item, Iterable):
            yield from deep_flatten(item)
        else:
            yield item


if __name__ == '__main__':
    #test = (0, (1, (2, 3)), [4])
    test = [[(1, 2), (3, 4)], [(5, 6), (7, 8)]]
    for x in deep_flatten(test):
        print(f'{x}')
    #test = deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])
