class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(arr,s,e):
            while s < e:
                arr[s],arr[e] = arr[e],arr[s]
                s,e = s + 1, e - 1
        
        k %= len(nums)
        reverse(nums,0,len(nums) - 1)
        reverse(nums,0,k - 1)
        reverse(nums,k,len(nums) - 1)