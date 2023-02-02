class MyHashSet:

    def __init__(self):
        self.head=[]
    def add(self, key: int) -> None:
        if key not in self.head:
            self.head.append(key)
    def remove(self, key: int) -> None:
        if key in self.head:
            self.head.remove(key)
    def contains(self, key: int) -> bool:
        return key in self.head
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)