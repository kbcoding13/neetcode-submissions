class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = n

        res = (res >> 16) | (res << 16) & 0xFFFFFFFF
        #swap the left 16 bits with the right 16 bits and OR with shift left 16

        res = ((res & 0xff00ff00) >> 8) | ((res & 0x00ff00ff) << 8)
        #swap adjacent bytes, mask with oxff00ff00 to get even bytes, shift right 8

        res = ((res & 0xf0f0f0f0) >> 4) | ((res & 0x0f0f0f0f) << 4)
        #swap adjacent nibbles (4-bit groups); mask with 0xf0f0f0f0 for upper nibbles, shift right 4

        res = ((res & 0xcccccccc) >> 2) | ((res & 0x33333333) << 2)
        #swap adjacent pairs of bits: mask with 0xcccccccc for pairs starting at even positions shift right 2

        res = ((res & 0xaaaaaaaa) >> 1) | ((res & 0x55555555) << 1)
        #swap adjacent bits: mask with 0xaaaaaaaa for odd positions, shift right 1

        return res & 0xFFFFFFFF
        #Apply final mask 0xFFFFFFFF to ensure 32-bit result, returning 964176192.