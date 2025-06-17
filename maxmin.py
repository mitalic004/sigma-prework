nums1 = [2, 4, 1, 0, 2, -1]
nums2 = [20, 50, 12, 6, 14, 8]
nums3 = [100, -100]


def maxminfind(ls_num):
    min_num = ls_num[0]
    max_num = ls_num[0]

    for num in ls_num:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    return [min_num, max_num]


print(maxminfind(nums1))
print(maxminfind(nums2))
print(maxminfind(nums3))
