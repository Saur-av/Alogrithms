'''You are given two integer arrays nums1 and nums2,
sorted in non-decreasing order,
and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.
'''


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        '''
        Time Complexity : O(m + n)
        Space Complexty : O(m)'''
        temp = nums1[:m]
        i = 0
        j = 0
        cur = 0

        #Loop through the arrays and fill from start
        while (i < m and j < n):
            if temp[i] < nums2[j]:
                nums1[cur] = temp[i]
                i += 1
            else:
                nums1[cur] = nums2[j]
                j += 1
            cur += 1
        
        # if temp still has items then
        if (i < m):
            nums1[cur:] = temp[i:]
        # if nums2 still has items then
        if (j < n):
            nums1[cur:] = nums2[j:]