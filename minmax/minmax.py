def minmax(num):
    try:
        num = sorted(num)
        min = num[0]
        max = num[-1]
    except IndexError:
        raise ValueError

    return min, max


if __name__ == '__main__':
    #min, max = minmax([4.4, 1, 2, 3, 4])
    min, max = minmax({8, 7, 5, 3, 9, 6, 2})
    print(f'{min}, {max}')