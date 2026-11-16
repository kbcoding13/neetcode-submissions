class Solution:
    def reverseBits(self, n: int) -> int:
        binaryStr = f"{n:032b}"
        reversedStr = binaryStr[::-1]
        return int(reversedStr, 2)