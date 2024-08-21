'''
Given an integer array nums sorted in non-decreasing order,
remove some duplicates in-place such that each unique element appears at most twice.
The relative order of the elements should be kept the same.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        '''
        Time Complexity : Linear | O(n)
        Space Complexity : Constant | O(1)'''
        curr = 0
        last = None

        for i in range(len(nums)):
            if nums[i] == last:
                if curr - 2 >= 0 and nums[curr - 2] == last:
                    continue
            
            nums[curr] = nums[i]
            curr += 1
            last = nums[i]
        
        return curr
    

def test(nums):
    print("\nnums =",nums)
    ans = Solution.removeDuplicates(1,nums)
    print("Final solution =",nums[:ans])

test([1,1,1,2,2,3])
test([0,0,1,1,1,1,2,3,3])