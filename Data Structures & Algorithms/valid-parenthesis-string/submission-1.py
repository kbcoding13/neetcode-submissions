class Solution:
    def checkValidString(self, s: str) -> bool:
        
        cmin = 0
        cmax = 0

        for st in s:
            if st == '(':
                cmax += 1
                cmin += 1
            elif st == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            else:
                cmax += 1
                cmin = max(cmin - 1, 0)
        
            if cmax < 0:
                return False
        
        return cmin == 0