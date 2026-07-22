class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list = []
        for num in nums:
            if num in list:
                return True
            else:
                list.append(num)
        return False