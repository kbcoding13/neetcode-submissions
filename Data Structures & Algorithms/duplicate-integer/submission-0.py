class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        added_nums = []
        for i in nums:
            if i not in added_nums:
                added_nums.append(i)
        if len(nums) == len(added_nums):
            return False
        else:
            return True
                