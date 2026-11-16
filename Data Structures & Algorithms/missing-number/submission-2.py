class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        
        res = len(nums)
        for i in range(len(nums)):
            if nums[i] != i:
                res = i
                break
    
        return res