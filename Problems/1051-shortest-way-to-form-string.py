# https://leetcode.com/problems/shortest-way-to-form-string

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        char2id = dict()
        for i in range(len(source)):
            try:
                char2id[source[i]].append(i)
            except:
                char2id[source[i]] = [i]
        
        res = 1
        cur_idx = -1
        
        for c in target:
            if c not in char2id:
                return -1
            
            found = False
            while not found:
                for idx in char2id[c]:
                    if idx > cur_idx:
                        found = True
                        cur_idx = idx
                        # print(cur_idx)
                        break
                        
                if not found:
                    cur_idx = -1
                    res += 1
        
        return res