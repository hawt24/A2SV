class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        num_fresh_orange=0
        que=deque()
        ans=0
        for i in  range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    que.append([i,j])
                if grid[i][j]==1:
                    num_fresh_orange+=1
                    
        while que and num_fresh_orange>0:
            
            for i in range(len(que)):
                
                r,c=que.popleft()
                
                for ro,co in directions:
                    row=ro+r
                    col=co+c
                    if row<0 or col<0 or row==len(grid) or col==len(grid[0]) or grid[row][col]!=1:
                        continue
                    que.append([row,col])
                    grid[row][col]=2
                    num_fresh_orange-=1
            ans+=1
        if num_fresh_orange==0:
            return ans
        else:
            return -1

                    
                    
                    
     
        
                    
                
        
                    
                    
                    

                    
      
                               