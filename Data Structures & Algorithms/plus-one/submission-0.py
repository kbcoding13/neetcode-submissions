class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits[len(digits) - 1] != 9:
            digits[len(digits) - 1] += 1
            return digits

        digits[len(digits) - 1] = 0
        carry = 1

        for i in range(len(digits) - 2, -1, -1):
            if digits[i] < 9:
                digits[i] += carry
                return digits
            else:
                digits[i] = 0
        
        digits[0] = 1
        digits.append(0)

        return digits