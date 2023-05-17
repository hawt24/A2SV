class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(int)
        
        def find(x):
            if x not in graph:
                graph[x]=x
                
            while graph[x]!=x:
                graph[x]=graph[graph[x]]
                x=graph[x]
                
            return x
        
        def union(x,y):
            p1,p2=find(x),find(y)
            if p1>p2:
                graph[p1]=p2
            else:
                graph[p2]=p1
                
        for i,j in edges:
            union(i,j)
                
        return find(source)==find(destination)
    

            
        

            
        
            
            
            