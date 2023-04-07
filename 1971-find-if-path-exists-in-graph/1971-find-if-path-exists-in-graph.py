class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n==1:
            return True
        graph=defaultdict(list)
        for sorce,dest in edges:
            graph[sorce].append(dest)
            graph[dest].append(sorce)
            
        flag=False
        def dfs(arr):
            nonlocal flag,graph
            for i in arr:
                if i==destination:
                    flag=True
                    return
                if i not in  visted:
                    visted.add(i)
                    dfs(graph[i])
        visted=set()
        dfs(graph[source])
        return flag
  
            
        
            
            
            