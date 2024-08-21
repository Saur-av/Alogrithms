'''Given an integer array nums and an integer val,
remove all occurrences of val in nums in-place.
The order of the elements may be changed.
Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k,
to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.'''

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        '''
        Time Complexity : Linear | O(n)
        Space Complexiy : Constant | O(1)'''
        pointer = 0 #Keep track of where we are in array

        for i in range(len(nums)): 
        #Loop through array and update the vale at pointer if item is not eqauls to val
            if nums[i] != val:
                nums[pointer] = nums[i]
                pointer += 1

        return pointer

def test(nums,val):
    print("\nnums =",nums)
    print("val =",val)

    ans = Solution.removeElement(1,nums,val)

    print("Solution Array =",nums[:ans])

test(nums = [0,1,2,2,3,0,4,2], val = 2)
test(nums = [3,2,2,3], val = 3)