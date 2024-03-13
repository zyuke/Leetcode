# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window = [c for c in s[:k]]
        vowels = set(['a', 'e', 'i', 'o','u'])
        cur_count, max_count = 0, 0
        for c in window:
            if c in vowels:
                cur_count += 1
        max_count = max(cur_count, max_count)

        for c in s[k:]:
            window.append(c)
            if c in vowels:
                cur_count += 1
            head = window.pop(0)
            if head in vowels:
                cur_count -= 1
            max_count = max(cur_count, max_count)
        
        return max_count