class Solution:
    def mySqrt(self, x: int) -> int:
        left=1
        right=x
        ans=0
        while left<=right:
            mid=(left+right)//2
            sqr=mid**2

            if sqr>x:
                right=mid-1
            elif sqr<x:
                ans=mid
                left=mid+1
            else:
                return mid
        return ans
                
                
                
                