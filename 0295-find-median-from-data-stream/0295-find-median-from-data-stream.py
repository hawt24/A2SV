class MedianFinder:

    def __init__(self):
        self.arr=[]

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        
        
    def findMedian(self) -> float:
        self.arr.sort()
        if len(self.arr)==1:
            return self.arr[0]

        if len(self.arr)%2==0:
            mid=len(self.arr)//2
            num1=self.arr[mid]
            num2=self.arr[mid-1]
            return (num1+num2)/2
        else:
            return self.arr[len(self.arr)//2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()