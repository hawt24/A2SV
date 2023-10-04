class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            temp = ord(char) - ord('a')
            if temp not in curr.children:
                curr.children[temp] = TrieNode()
            curr = curr.children[temp]
            curr.count += 1

    def search(self, word: str, count: int) -> int:
        curr = self.root
        for char in word:
            temp = ord(char) - ord('a')
            count += curr.children[temp].count
            curr = curr.children[temp]
        return count

class Solution:
    def __init__(self):
        self.trie = Trie()

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        for word in words:
            self.trie.insert(word)
        result = []
        for word in words:
            count = 0
            count = self.trie.search(word, count)
            result.append(count)
        return result
