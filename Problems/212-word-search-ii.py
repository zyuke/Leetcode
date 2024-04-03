class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEndOfWord = False
 

class Trie:
    def __init__(self):
        self.root = self.getNode()
 
    def getNode(self):
        return TrieNode()
 
    def insert(self, key):
        curNode = self.root
        for char in key:
            if not char in curNode.children:
                curNode.children[char] = self.getNode()
            curNode = curNode.children[char]
        curNode.isEndOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        M, N = len(board), len(board[0])
        T = Trie()
        for word in words:
            T.insert(word)
        res = set()

        def dfs(i: int, j: int, curNode: TrieNode, curWord: str):
            if board[i][j] in curNode.children:
                curWord += board[i][j]
                curNode = curNode.children[board[i][j]]
                if curNode.isEndOfWord:
                    res.add(curWord)
                memo = board[i][j]
                board[i][j] = '#'
                for (di, dj) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    newi, newj = i + di, j + dj
                    if 0 <= newi < M and 0 <= newj < N:
                        if board[newi][newj] != '#' and board[newi][newj] in curNode.children:
                            dfs(newi, newj, curNode, curWord)
                board[i][j] = memo

        for i in range(M):
            for j in range(N):
                dfs(i, j, T.root, '')

        return list(res)
