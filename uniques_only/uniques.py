def old_uniques_only(lst):
    return list(dict.fromkeys(lst))


def uniques_only(lst):
    found = []
    for x in lst:
        if x not in found:
            yield x
            found.append(x)


if __name__ == '__main__':
    tmp = uniques_only([1, 2, 2, 1, 1, 3, 2, 1])
    print(f'{tmp}')
