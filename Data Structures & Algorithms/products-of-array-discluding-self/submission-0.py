class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        #PREFIXES
        prefixes = 1
        for i in range(len(nums)):
            res[i] = prefixes
            prefixes *= nums[i]

        #SUFFIXES
        suffixes = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffixes
            suffixes *= nums[i]

        return res