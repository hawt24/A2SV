class Solution:
    def fun(self,piles,k,h):
        summ=0
        for i in piles:
            t = i // k
            if i%k!=0:
                t+=1 
            summ +=t
        return summ<=h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right=max(piles)
        left=1
        ans=0
        while left<=right:
            mid=(left+right)//2
            if self.fun(piles,mid,h):
                right=mid-1
                ans=mid
            else:
                left=mid+1
        return ans
                
                
                
            
                
        