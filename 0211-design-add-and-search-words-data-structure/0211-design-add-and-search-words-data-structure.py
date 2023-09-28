class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEnded = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isEnded = True

    def search(self, word: str) -> bool:
        
        return self.search_recursive(self.root, word)

    def search_recursive(self, node: TrieNode, word: str) -> bool:
        if not word:
            return node.isEnded

        char = word[0]
        if char == '.':
            for child in node.children:
                if child and self.search_recursive(child, word[1:]):
                    return True
        else:
            index = ord(char) - ord('a')
            if node.children[index]:
                return self.search_recursive(node.children[index], word[1:])

        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)