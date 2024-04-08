class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append((c, i))
            if c == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append((c, i))
        
        res = ""
        prev = 0
        for (_, idx) in stack:
            res += s[prev:idx]
            prev = idx + 1
        res += s[prev:]
        return res

