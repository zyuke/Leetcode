from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)
        pattern = dict()
        for word in wordList:
            for i in range(len(word)):
                p = word[:i] + '*' + word[i+1:]
                if p in pattern:
                    pattern[p].append(word)
                else:
                    pattern[p] = [word]
            
        graph = defaultdict(lambda: [])
        for p in pattern:
            for i in range(len(pattern[p])):
                for j in range(i, len(pattern[p])):
                    graph[pattern[p][i]].append(pattern[p][j])
                    graph[pattern[p][j]].append(pattern[p][i])

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        while queue:
            word, d = queue.popleft()
            if word == endWord:
                return d
            for next_word in graph[word]:
                if next_word not in visited:
                    queue.append((next_word, d+1))
                    visited.add(next_word)

        return 0
