class LUPrefix:

    def __init__(self, n: int):
        self.ans=0
        self.temp=[False]*(n+1) 
        

    def upload(self, video: int) -> None:
        video-=1
        self.temp[video]=True
        while self.temp[self.ans]:
            self.ans+=1
            
    def longest(self) -> int:
        return self.ans
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()