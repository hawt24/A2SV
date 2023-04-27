class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        #         def bfs(node):
        #             visited=set()
        #             que=deque()
        #             while que:
        #                 key=que.popleft()


        #             for key in rooms[node]:
        #                 if key not in visited:
        #                     visited.add(key)
        #                     que.apppend(key)
        #                 bfs(key)
        visited=set()
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for key in rooms[node]:
                dfs(key)
                
        dfs(0)
        return len(rooms)==len(visited)
            

            
            
            