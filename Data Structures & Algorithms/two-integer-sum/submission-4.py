class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            indices[nums[i]] = i
        
        for i in range(len(nums)):
            desired_number = target - nums[i]
            if desired_number in nums:
                j = indices[desired_number]
                if i != j:
                    return [i, j]
        
        


    