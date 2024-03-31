class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [] 
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)

        if not stack:
            res = len(s)
        else:
            res = 0
            l = -1
            stack.append(len(s))
            for idx in stack:
                res = max(res, idx-l-1)
                l = idx

        return res

