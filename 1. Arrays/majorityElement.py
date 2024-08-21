'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
'''

class Solution:
    '''Since the majority elements are always greater, we use a voting system.
    This works because either majority numbers appear linear one after another OR
    The majority item is in last of array.
    
    [1,1,2,1,2] : 1 appear linear, then the value of Candidate is always 1.
    [1,2,1,2,1] : If the majority items are not linear, it is always in the end of array.'''
    def majorityElement(self, nums: list[int]) -> int:
        '''
        Time Complexity : Linear | O(n)
        Space Complexity : Constant | O(1)'''
        can = 0
        count = 0

        #Since majority of elemets are always greater
        for i in range(len(nums)):
            if count == 0:
                can = nums[i]
                continue

            can += 1 if can == nums[i] else -1
        
        return can

def test(num):
    print(f"\nnum = {num} \nThe majority element is {Solution.majorityElement(1,num)}.")

test([1,2,2,3,21,213,12,312,312,1,1,312,312,312])
test([2,2,1,1,1,2,2])