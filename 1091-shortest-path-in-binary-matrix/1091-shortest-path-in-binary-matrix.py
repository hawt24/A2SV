class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        que=deque()
        visited=set()
        direction=[(1,0),(0,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1),(1,1)]
        if grid[0][0]==0:
            que.append((1,(0,0)))
       
        while que:
            lenght,pos=que.popleft()
            r=pos[0]
            c=pos[1]
            if (r,c) ==(len(grid)-1,len(grid[0])-1):
                return lenght
                
            for i,j in direction:
                new_r=r+i
                new_c=c+j
                if 0<=new_r<len(grid) and 0<=new_c<len(grid[0]) and (new_r,new_c) not in visited and grid[new_r][new_c]==0:

                    que.append((lenght+1,(new_r,new_c)))
                    visited.add((new_r,new_c))
        return -1

            
            
            