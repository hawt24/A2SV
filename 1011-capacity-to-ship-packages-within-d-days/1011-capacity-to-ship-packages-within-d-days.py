class Solution:
    def func(self,weights,k,days):
        summ=1
        total=0
        for i in weights:
            total+=i
            if total>k:
                total=i
                summ+=1
        return summ<=days
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        ans=0
        while left<=right:
            mid=(left+right)//2
            if self.func(weights,mid,days):
                right=mid-1
                ans=mid
            else:
                left=mid+1
                
        return right+1
        
                