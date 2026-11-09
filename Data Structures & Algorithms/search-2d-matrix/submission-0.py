class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix) - 1

        while l <= r:

            m = l + (r - l) // 2

            if matrix[m][len(matrix[m]) - 1] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else:
                for num in matrix[m]:
                    if num == target:
                        return True
                return False
        return False