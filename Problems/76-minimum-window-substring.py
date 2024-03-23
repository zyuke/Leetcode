class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        t_chars = defaultdict(lambda: 0)
        for c in t:
            t_chars[c] += 1
        
        def cp_chars(t_chars, window_chars):
            for c in t_chars:
                if t_chars[c] > window_chars[c]:
                    return False
            return True

        window_chars = defaultdict(lambda: 0)
        left, right = 0, 0
        min_size = float('inf')
        min_left, min_right = -1, -1
        n = len(s)

        while True:
            if right >= n:
                break

            window_chars[s[right]] += 1

            while cp_chars(t_chars, window_chars):
                if right - left < min_size:
                    min_left, min_right = left, right
                    min_size = right - left
                window_chars[s[left]] -= 1
                left += 1
            
            right += 1

        if min_left == -1 and min_right == -1:
            return ""
        
        return s[min_left:min_right+1]

