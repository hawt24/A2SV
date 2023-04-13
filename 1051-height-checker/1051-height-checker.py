class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans=0
        temp=sorted(heights)
        for idx,val in enumerate(temp):
            if heights[idx]!=val:
                ans+=1
        return ans
 
   