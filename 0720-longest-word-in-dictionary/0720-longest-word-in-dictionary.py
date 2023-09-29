class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnded = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.word = ""
        
    def insert(self, word:str):
        curr = self.root
        for i in word:
            temp = ord(i) - 97
            
            if temp not in curr.children:
                curr.children[temp] = TrieNode()
                
            curr = curr.children[temp]
        curr.isEnded = True
    
    def dfs(self, node, path):
        if node.isEnded:
            if len(path) > len(self.word):
                self.word = path
            elif len(path) == len(self.word):
                if path < self.word:
                    self.word = path
                    
        for key, nodes in node.children.items():
            if not nodes.isEnded:
                continue
            self.dfs(nodes, path + chr(key+97))
    
    def longest(self):
        
        self.dfs(self.root, self.word)
        return self.word

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.longest()
