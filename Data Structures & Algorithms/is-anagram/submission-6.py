class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_chars = {}
        t_chars = {}

        for char in s:
            if char not in s_chars:
                s_chars[char] = 1
            else:
                s_chars[char] += 1

        for char in t:
            if char not in t_chars:
                t_chars[char] = 1
            else:
                t_chars[char] += 1

        for char in s_chars:
            if char not in t_chars or s_chars[char] != t_chars[char]:
                return False
        return True