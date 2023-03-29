class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[]
        def changeToBit(n):
            temp=[]
            while n:
                temp.append(n%2)
                n=n//2
            temp[::-1]
            return temp
        
        for i in range(n+1):
            te = changeToBit(i)
            ans.append(te.count(1))
        return ans
        
            
            
          