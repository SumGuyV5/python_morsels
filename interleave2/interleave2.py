def interleave(nums1, nums2):
    for x, y in zip(nums1, nums2):
        yield x
        yield y