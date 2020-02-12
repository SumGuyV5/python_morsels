def old_chunked(numbers, n):
    for i in range(0, len(numbers), n):
        yield numbers[i:i+n]

def chunked(numbers, n):
    iterators = [iter(numbers)] * n
    return iterators

if __name__ == '__main__':
    for chunk in chunked([1, 2, 3, 4, 5], n=2):
        print(*chunk)

    squares = (n ** 2 for n in range(6))
    for chunk in chunked(squares, 3):
        print(*chunk)
