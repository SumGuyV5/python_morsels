def float_rangeold(start, end, increment):
    rtn = []
    current = start
    rev = False
    if increment < 0:
        rev = True
        increment *= float(-1)

    while current < end:
        rtn.append(current)
        current += increment

    if rev:
        return list(reversed(rtn))

    return rtn


def float_rangeold2(*args):
    numargs = len(args)
    if numargs == 0:
        raise TypeError("you need to write at least a value")
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError("Inclusive range was expected at most 3 arguments,got {}".format(numargs))
    i = start
    length = (stop - start) / step
    while True:
        if step < 0 and i < stop or step > 0 and i >= stop:
            break
        yield i
        i += step


class float_range:
    def __init__(self, *args):
        numargs = len(args)
        if numargs == 0:
            raise TypeError("you need to write at least a value")
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else:
            raise TypeError("Inclusive range was expected at most 3 arguments,got {}".format(numargs))

    def __len__(self):
        length =  int(round((self.stop - self.start) / self.step))
        if length < 0:
            return 0
        return length

    def __iter__(self):
        i = self.start
        while True:
            if self.step < 0 and i <= self.stop or self.step > 0 and i >= self.stop:
                break
            yield i
            i += self.step

    def __reversed__(self):
        pass

    def __eq__(self, other):
        if isinstance(other, float_range):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)


if __name__ == '__main__':
    for n in float_range(0.5, 2.5, 0.5):
        print(n)

    print(list(reversed(float_range(0.5, 2.5, 0.5))))
   #len(float_range(1, 6, -1))
   #for n in float_range(1, 6, -1):
   #     print(n)
