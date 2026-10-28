class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def backtrack(index: int, current_sum:int):
            if index == len(nums):
                if current_sum == target: 
                    return 1 
                else:
                    return 0
            
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]

            result = backtrack(index + 1, current_sum + nums[index]) + \
                backtrack(index + 1, current_sum - nums[index])
            
            memo[(index, current_sum)] = result
            
            return result
        
        return backtrack(0, 0)