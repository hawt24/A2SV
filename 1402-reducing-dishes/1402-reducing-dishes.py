class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        ans=0
        curr=0
        while satisfaction and  satisfaction[-1] +curr>0:
            curr+=satisfaction.pop()
            ans+=curr
        return ans
        