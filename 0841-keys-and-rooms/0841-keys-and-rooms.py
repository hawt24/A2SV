class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited=set([0])
        
        def bfs(node):
            nonlocal visited
            que=deque([0])
            
            while que:
                key=que.popleft()
                for i in rooms[key]:
                    if i not in visited:
                        visited.add(i)
                        que.append(i)
                        
        bfs(0)
        return len(visited)==len(rooms)
                
        
        
        
        
        
        
        
        
        

            

            
            
            