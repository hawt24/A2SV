class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res=float('inf') #we can compare infinity to the manhattan distance
        ans=-1
        for i,(x1,y1) in enumerate (points):
            if x==x1 or y==y1:
                dist=abs(x-x1)+abs(y-y1)
                if dist<res:
                    ans=i
                    res=dist
        return ans
                
                
                