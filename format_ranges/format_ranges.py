def rang(numbers):
    rtn = []
    first = last = numbers[0]
    for n in numbers[1:]:
        if n - 1 == last:  # Part of the group, bump the end
            last = n
        else:  # Not part of the group, yield current group and start a new
            rtn.append((first, last))
            first = last = n
    rtn.append((first, last))

    return sorted(rtn)


def format_ranges(numbers):
    rtn = rang(sorted(numbers))
    return ",".join(
        f"{start}-{end}" if start != end else f"{start}"
        for (start, end) in rtn
    ) # Yield the last group

if __name__ == '__main__':
    print(f'{format_ranges([1, 3, 5, 6, 8])}')
