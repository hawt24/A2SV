class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        arr=[-1]*len(graph)
        print(arr)
        
        def dfs(i):
            for child in graph[i]:
                print(child)
                if arr[child]==-1:
                    if arr[i]==0:
                        arr[child]=1
                    else:
                        arr[child]=0
                        
                    if not dfs(child):
                        return False
                elif arr[i]==arr[child]:
                    return False
            return True
        
        for i in range(len(graph)):
            if arr[i]==-1:
                arr[i]=0
                if not dfs(i):
                    return False
        return True
                 
            
                
            
        
        

        
        
     
            
        
        
        