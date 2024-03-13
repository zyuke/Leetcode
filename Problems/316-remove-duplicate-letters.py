# https://leetcode.com/problems/remove-duplicate-letters

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c2lastIdx = {}
        for i in range(len(s)):
            c2lastIdx[s[i]] = i
        stack = []
        seen = set()
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1][0] and i < c2lastIdx[stack[-1][0]]:
                    temp = stack.pop()
                    seen.remove(temp[0])
                stack.append((c, i))
                seen.add(c)
        res = ""
        for c, _ in stack:
            res += c
        return res