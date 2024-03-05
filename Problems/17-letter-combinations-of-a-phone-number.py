// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': ['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        
        if digits == '':
            return []
        
        def dfs(s, cur_word, res):
            if s == '':
                res.append(cur_word)
                return
            for c in mapping[s[0]]:                
                dfs(s[1:], cur_word + c, res)
            
        res = []
        dfs(digits, '', res)
        return res