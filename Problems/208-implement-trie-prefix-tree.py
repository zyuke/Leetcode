class TrieNode:

    def __init__(self):
        self.children = dict()
        self.isEndOfWord = False

        
class Trie:

    def __init__(self):
        self.root = self.getNode()
 
    def getNode(self):
        return TrieNode()

    def insert(self, word):
        curNode = self.root
        for char in word:
            if not char in curNode.children:
                curNode.children[char] = self.getNode()
            curNode = curNode.children[char]
        curNode.isEndOfWord = True

    def search(self, word: str) -> bool:
        curNode = self.root
        for char in word:
            if not char in curNode.children:
                return False
            curNode = curNode.children[char]
        return curNode.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for char in prefix:
            if not char in curNode.children:
                return False
            curNode = curNode.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
