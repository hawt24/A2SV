class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        area=0
        maxmarea=0
        while left<=right:
            if height[left]>height[right]:
                area=(right-left)*height[right]
                right-=1
            else:
                area=(right-left)*height[left]
                left+=1
            maxmarea=max(area,maxmarea)
        return maxmarea
            