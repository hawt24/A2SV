class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[i for i in range(1,n+1)]
        start=0
        temp=0
        while len(arr)!=1:
            temp=(start+k-1)%len(arr)
            arr.pop(temp)
            start=temp
        return arr[0]
            