from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(lambda: 0)
        for c in s:
            count[c] += 1
        res = 0
        lone = False
        for c in count:
            if count[c] % 2 == 0:
                res += count[c]
            else:
                res += count[c]-1
                lone = True

        if lone:
            res += 1
        return res
