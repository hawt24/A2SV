class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph=defaultdict(list)
        
        for i in range(len(bombs)):
            xi,yi,zi=bombs[i]
            
            for j in range(len(bombs)):
                xj,yj,zj=bombs[j]
                
                if i!=j and (((xi-xj)**2)+((yi-yj)**2))<=zi**2:
                    graph[i].append(j)
                    
            
        def dfs(node):
            nonlocal visited
            cnt=1
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    cnt+=dfs(i)
            return cnt
        
        ans=0
        for i in range(len(bombs)):
            visited=set()
            dfs(i)
            ans=max(ans,len(visited))
        return ans
        