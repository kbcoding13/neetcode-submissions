class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(i, current_sum, current_array):

            if current_sum == target:
                res.append(current_array)
                return
            
            if current_sum > target:
                return

            for n in range(i, len(nums)):
                backtrack(n, current_sum + nums[n], current_array + [nums[n]])


       
        backtrack(0, 0, [])
        
        return res