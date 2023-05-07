class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        direction=[(1,0),(0,1),(0,-1),(-1,0)]
        que=deque()
        que.appendleft([entrance[0],entrance[1]])
        
        visited=set((entrance))
        
        ans=0
        while que:
            for _ in range(len(que)):
            
                row,col =que.pop()

                if (row!= entrance[0] or col!= entrance[1]) and ((row == 0) or (col == 0) or (row==len(maze)- 1) or (col==len(maze[0])-1)):
                        return ans

                for i,j in direction:
                    new_r=i+row
                    new_c=j+col

                    if 0<=new_r<len(maze) and 0<=new_c<len(maze[0]) and maze[new_r][new_c]=="." and (new_r,new_c) not in visited:

                        visited.add((new_r,new_c))
                        que.appendleft([new_r,new_c])
            ans+=1
            
        return -1

                    
                
            
            
            