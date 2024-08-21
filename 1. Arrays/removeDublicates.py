'''
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted,
you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements
in the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        '''
        Time Complexity : Linear | O(n)
        Space Complexity : Constant | O(1)'''
        curr = 0 # Pointer
        lastItem = None
        for i in range(len(nums)):
            if lastItem == nums[i]: continue
            nums[curr] = nums[i]
            curr += 1
            lastItem = nums[i]
        
        return curr

def test(nums):
    print("\nnums =",nums)
    ans = Solution.removeDuplicates(1,nums)
    print("Solution Array =",nums[:ans])

test([1,1,2])
test([0,0,1,1,1,2,2,3,3,4])