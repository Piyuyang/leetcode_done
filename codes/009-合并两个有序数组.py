# -*- coding:utf-8 -*-
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5

def merge(nums1, m, nums2, n):
    # nums1[:] = nums1[:m]
    # if m == 0:
    #     nums1[:] = nums2[:]
    # cur1, cur2 = 0, 0
    #
    # while cur2 < n and cur1 < m:
    #     if nums2[cur2] < nums1[cur1]:
    #         nums1.insert(cur1, nums2[cur2])
    #         cur2 += 1
    #         cur1 += 1
    #     elif cur1 < m-1 and nums1[cur1] <= nums2[cur2] < nums1[cur1+1]:
    #         nums1.insert(cur1+1, nums2[cur2])
    #         cur2 += 1
    #         cur1 += 2
    #     else:
    #         cur1 += 1
    #     m = len(nums1)
    # if cur2 < n:
    #     nums1[cur1+1:] = nums2[cur2:]

    nums1_copy = nums1[:m]
    nums1[:] = []
    cur1, cur2 = 0, 0
    while cur1 < m and cur2 < n:
        if nums1_copy[cur1] < nums2[cur2]:
            nums1.append(nums1_copy[cur1])
            cur1 += 1
        else:
            nums1.append(nums2[cur2])
            cur2 += 1
    if cur1 < m:
        nums1[cur1+cur2:] = nums1_copy[cur1:]
    if cur2 < n:
        nums1[cur1+cur2:] = nums2[cur2:]
    print(id(nums1))


print(id(nums1))
merge(nums1, m, nums2, n)
print(nums1,id(nums1))

