class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indices = {}

        for ind, num in enumerate(numbers):
            indices[num] = ind

        for i in range(len(numbers)):
            difference = target - numbers[i]
            if difference in indices and indices[difference] != i:
                return [min(indices[difference] + 1, i + 1), max(indices[difference] + 1, i + 1)]