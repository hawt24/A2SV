class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        mid=image[sr][sc]
        row=len(image)
        col=len(image[0])
        viseted=set()
        
        def dfs(sr,sc):
            if  sr<0 or sr>=row or sc<0 or sc>=col or (sr,sc) in viseted:
                return
            if image[sr][sc]!=mid:
                return
            
            image[sr][sc] = color
            viseted.add((sr,sc))
            dfs(sr+1, sc)
            dfs(sr-1, sc)
            dfs(sr, sc+1)
            dfs(sr, sc-1)
        
                
        dfs(sr,sc)
            
    
        return image
            
            
        