#!/usr/bin/env python
# coding:utf-8
from typing import List


class Solution:
    def merge(self, nums1, m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1, p2 = 0, 0
        sortedarr = []

        if nums2 == []:
            nums1[:] = nums1[:]
        elif nums1 == []:
            nums1[:] = nums2[:]
        else:
            while p1 < m or p2 < n:
                if p1 == m:
                    sortedarr.append(nums2[p2])
                    p2 += 1
                elif p2 == n:
                    sortedarr.append(nums1[p1])
                    p1 += 1
                elif nums1[p1] < nums2[p2]:
                    sortedarr.append(nums1[p1])
                    p1 += 1
                else:
                    sortedarr.append(nums2[p2])
                    p2 += 1
            nums1[:] = sortedarr

        print(nums1)
        return nums1

if __name__ == '__main__':
    sol = Solution()
    sol.merge([2],1,[1],1)