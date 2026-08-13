class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.strip().lower()

        i = 0
        j = len(string) - 1
        while j > i:
            if not string[i].isalnum():
                i += 1
                continue
            if not string[j].isalnum():
                j -= 1
                continue
            else:
                if string[i].lower() == string[j].lower():
                    i += 1
                    j -= 1
                else:
                    return False
        return True