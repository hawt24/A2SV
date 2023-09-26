class TrieNode:
    def __init__(self):        
        self.children=[None for i  in range(26)]
        self.isEndedOfWord=False
    

class Trie:

    def __init__(self):
        self.root=TrieNode()
        
    def insert(self, word: str) -> None:
        
        curr= self.root
        for i in word:
            temp=ord(i)-97
            if not curr.children[temp]:
                curr.children[temp]=TrieNode()
            curr=curr.children[temp]
                
        curr.isEndedOfWord=True

    def search(self, word: str) -> bool:
        
        current  = self.root
        
        for c in word:
            
            index = ord(c) - 97
            
            if current.children[index]:
                
                current = current.children[index]
                
            else:
                
                return False
        return current.isEndedOfWord
            
    def startsWith(self, prefix: str) -> bool:
        current  = self.root
        
        for c in prefix:
            
            index = ord(c) - 97
            
            if current.children[index]:
                
                current = current.children[index]
                
            else:
                
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)