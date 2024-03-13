# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        startWords_sorted = set()
        for word in startWords:
            startWords_sorted.add("".join(sorted(list(word))))
        
        targetWords_sorted = []
        for word in targetWords:
            targetWords_sorted.append(sorted(list(word)))
            
        res = 0
        for w in targetWords_sorted:
            for i in range(len(w)):
                new_w = w[:i] + w[i+1:]
                new_w = "".join(new_w)
                if new_w in startWords_sorted:
                    res += 1
                    break
        
        return res