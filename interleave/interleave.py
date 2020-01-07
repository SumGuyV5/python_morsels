def interleave_old(nums1, nums2):
    tmp = []
    for x, y in zip(nums1, nums2):
        tmp.append(x)
        tmp.append(y)

    return tmp


def interleave(nums1, nums2):
    for x, y in zip(nums1, nums2):
        yield x
        yield y


if __name__ == '__main__':
    t = interleave([1, 2, 3, 4], [5, 6, 7, 8])
    print(t)
    nums = [1, 2, 3, 4]
    t = interleave(nums, (n ** 2 for n in nums))
    print(t)