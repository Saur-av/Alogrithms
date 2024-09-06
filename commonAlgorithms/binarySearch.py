

def search(self, nums: list[int], target: int) -> int:
    '''
    Time Complexity : Logarithmic | O(log(n))
    Space Complexity : Constant | O(1)'''
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if target > nums[m]:
            l = m + 1
        else:
            r = m - 1
    
    return -1
