class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(s):
            return s == s[::-1]

        wordMap = {}
        for i, word in enumerate(words):
            wordMap[word] = i

        res = []
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                prefix = word[:j]
                suffix = word[j:]
                if isPalindrome(prefix):
                    suffixReverse = suffix[::-1]
                    if suffixReverse != word and suffixReverse in wordMap:
                        res.append([wordMap[suffixReverse], i])
                if j != len(word) and isPalindrome(suffix):
                    prefixReverse = prefix[::-1]
                    if prefixReverse != word and prefixReverse in wordMap:
                        res.append([i, wordMap[prefixReverse]])

        return res
