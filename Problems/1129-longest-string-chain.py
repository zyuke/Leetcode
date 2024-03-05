// https://leetcode.com/problems/longest-string-chain

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        word_set = set(words)
        words.sort(key=lambda x: len(x), reverse=True)
        word2len = dict()
        
        def dfs(w):
            if w in word2len:
                return word2len[w]
            max_len = 1
            for i in range(len(w)):
                new_w = w[:i] + w[i+1:]
                # print(new_w)
                if new_w in word_set:
                    cur_len = 1 + dfs(new_w)
                    max_len = max(max_len, cur_len)
            word2len[w] = max_len
            
            return max_len
        
        for w in words:
            dfs(w)
        
        return max([word2len[w] for w in word2len])
            