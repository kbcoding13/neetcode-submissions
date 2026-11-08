class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        res = []

        def backtrack(i, current_sum, current_array):

            if current_sum == target:
                res.append(current_array)
            
            if current_sum > target:
                return

            for n in range(i, len(nums)):
                backtrack(n, current_sum + nums[n], current_array + [nums[n]])


        for i in range(len(nums)):
            backtrack(i, nums[i], [nums[i]])
        
        return res