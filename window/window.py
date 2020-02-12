def window(numbers, group_by):
    rtn = []

    for i in range(len(numbers)):
        if i + group_by <= len(numbers):
            break
        tmp = []
        for by in range(group_by):
            tmp.append(numbers[i+by])
        rtn.append(tuple(tmp))

    return rtn



if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6]
    squares = (n ** 2 for n in numbers)
    rtn = window(squares, 3)
    print(f'{rtn}')