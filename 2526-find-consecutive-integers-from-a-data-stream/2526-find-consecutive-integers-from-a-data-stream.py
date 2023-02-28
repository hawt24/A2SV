class DataStream:

    def __init__(self, value: int, k: int):
        self.k=k
        self.value=value
        self.que=deque()
        self.count=0
    def consec(self, num: int) -> bool:
        if len(self.que)==self.k and self.que.popleft()==self.value:
            self.count-=1
        if self.value == num:
            self.count+=1
        self.que.append(num)
        if self.count==self.k:
            return True
        return False
   

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)