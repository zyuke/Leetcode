class Solution:
    def checkValidString(self, s: str) -> bool:
        pmin, pmax = 0, 0
        for c in s:
            if c == '(':
                pmin += 1
                pmax += 1
            if c == ')':
                pmin -= 1
                pmax -= 1
            if c == '*':
                pmin -= 1
                pmax += 1
            if pmax < 0:
                return False
            pmin = max(0, pmin)
        return pmin == 0
