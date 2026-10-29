class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        indices = {}
        output = []

        for i in range(len(nums)):
            indices[nums[i]] = i
        
        for j in range(len(nums)):
            for k in range(len(nums)):
                if j == k:
                    continue
                diff = 0 - nums[j] - nums[k]
                if diff in indices:
                    if indices[diff] != k and indices[diff] != j:
                        trio = [diff, nums[j], nums[k]]
                        trio.sort()
                        if trio not in output:
                            output.append(trio)
        
        return output
                        