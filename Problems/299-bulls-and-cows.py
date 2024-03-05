// https://leetcode.com/problems/bulls-and-cows

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        cow = 0
        
        new_secret = ""
        new_guess = ""
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                new_secret += secret[i]
                new_guess += guess[i]
                
        count = dict()
        for i in range(len(new_secret)):
            try:
                count[new_secret[i]] += 1
            except:
                count[new_secret[i]] = 1
        
        for i in range(len(new_guess)):
            if new_guess[i] in count:
                if count[new_guess[i]] > 0:
                    cow += 1
                    count[new_guess[i]] -= 1
        
        return str(bull)+'A'+str(cow)+'B'