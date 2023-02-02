class MyHashMap:

    def __init__(self):
        self.head={}

    def put(self, key: int, value: int) -> None:
            self.head[key]=value
    def get(self, key: int) -> int:
        if key not in self.head:
            return -1
        else:
            return self.head[key]
    def remove(self, key: int) -> None:
        if key in self.head:
            self.head.pop(key)
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)