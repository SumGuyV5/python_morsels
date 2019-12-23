import types


def tail(elements, n):
    rv = []
    if n > 0:
        if isinstance(elements, types.GeneratorType):
            elements = [x for x in elements]
        n *= -1
        rv = elements[n:len(elements)]
        if isinstance(rv, str):
            rv = [char for char in rv]
        if type(elements) is tuple:
            return list(rv)

    return rv


if __name__ == "__main__":
    print(tail([1, 2, 3, 4, 5], 3))
    print(tail('hello', 2))
    print(tail('hello', 0))
    print(tail('hello', -2))

    squares = (n ** 2 for n in range(10))

    print(tail(squares, 3))

    print(tail((1, 2, 3), 3))
