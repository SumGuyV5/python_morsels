class Minmax:
    def __init__(self, min, max):
        self.min, self.max = min, max
    def __iter__(self):
        yield self.min
        yield self.max


def minmax(num):
    try:
        num = sorted(num)
        min = num[0]
        max = num[-1]
    except IndexError:
        raise ValueError

    return Minmax(min, max)


if __name__ == '__main__':
    #min, max = minmax([4.4, 1, 2, 3, 4])
    min, max = minmax({8, 7, 5, 3, 9, 6, 2})
    print(f'{min}, {max}')