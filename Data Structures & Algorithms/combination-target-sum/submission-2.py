class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(current_array, current_sum, index):

            if current_sum == target:
                res.append(current_array)
                return
            elif current_sum > target:
                return
            
            for i in range(index, len(nums)):
                backtrack(current_array + [nums[i]], current_sum + nums[i], i)

        backtrack([], 0, 0)

        return res