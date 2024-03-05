// https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        match = dict()
        used_words = set()
        if len(pattern) != len(words):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in match:
                if words[i] in used_words:
                    return False
                else:
                    match[pattern[i]] = words[i]
                    used_words.add(words[i])
                
            else:
                if match[pattern[i]] != words[i]:
                    return False
                
        return True