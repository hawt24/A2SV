class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        
        for u,v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
    
        visited=set()
    
        print(graph)
        ans=[]
        def dfs(node):
            nonlocal ans
            ans.append(node)
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    dfs(i)
            return ans
    
        for x,y in graph.items():
            if len(y)==1:
                return (dfs(x))
                
                
                
    
                    
            
                
            