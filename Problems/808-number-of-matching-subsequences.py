# https://leetcode.com/problems/number-of-matching-subsequences

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        buckets = [[] for _ in range(26)]
        for word in words:
            bucket_num = ord(word[0]) - 97
            buckets[bucket_num].append(word)
        
        res = 0
        for c in s:
            bucket_num = ord(c) - 97
            new_words = []
            for word in buckets[bucket_num]:
                if len(word) == 1:
                    res += 1
                else:
                    new_word = word[1:]
                    new_words.append(new_word)
            buckets[bucket_num] = []
            for word in new_words:
                new_bucket_num = ord(word[0]) - 97
                buckets[new_bucket_num].append(word)
        
        return res
                