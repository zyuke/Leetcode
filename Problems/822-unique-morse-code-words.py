# https://leetcode.com/problems/unique-morse-code-words

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        mapping = dict(zip(alphabet, morse))
        
        code = []
        for word in words:
            list_word = list(word)
            result = ""
            for alp in list_word:
                result += mapping[alp]
            code.append(result)
        n = set(code)
        return len(n)