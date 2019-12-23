def compact(data):
    val = []
    for x in data:
        if val:
            if x != val[-1]:
                val.append(x)
        else:
            val.append(x)

    return iter(val)


if __name__ == "__main__":
    print(compact([1, 1, 1]))
