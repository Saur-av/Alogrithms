'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] 
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers,
index1 and index2, added by one as an integer array [index1, index2] of length 2.
'''
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        '''
        Time Complexity : Linear | O(n)
        Space Complexity : Constant | O(1)'''
        l = 0
        r = len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return l + 1,r + 1
            
            if target - s < 0:
                r -= 1
            else:
                l += 1

def test(nums,tar,sol):
    print(f"\n nums = {nums}\ntarget = {tar}\nExpected = {sol}")
    res = Solution.twoSum(1,nums,tar)

    if not (res == sol):
        print("Test Case Failed!")

    print(f"Output : {res}")

test(nums = [2,3,4],tar = 6,sol = (1,3))
test(nums = [2,7,11,15],tar = 9,sol = (1,2))
test(nums = [-1,0],tar = -1,sol =(1,2))