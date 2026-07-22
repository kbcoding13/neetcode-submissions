class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_dupes = []
        for i in nums:
            if i not in non_dupes:
                non_dupes.append(i)
            else:
                return True
        return False