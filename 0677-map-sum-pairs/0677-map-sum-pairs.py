class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = 0
class MapSum:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, key: str, val: int) -> None:
        curr = self.root
        for char in key:
            idx = ord(char) - ord('a')
            if idx not in curr.children:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.value = val

    def sum(self, prefix: str) -> int:
        curr = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if idx not in curr.children:
                return 0
            curr = curr.children[idx]
        return self.getSum(curr)

    def getSum(self, node):
        if not node:
            return 0
        total = node.value
        for child in node.children.values():
            total += self.getSum(child)
        return total

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)