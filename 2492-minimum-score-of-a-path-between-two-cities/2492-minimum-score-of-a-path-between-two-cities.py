class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
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
                
        ans=float("inf")
        for i,j,k in roads:
            union(i,j)
            
        
        for i,j,k in roads:
            if find(i)==find(1) and find(j)==find(n):
                ans=min(ans,k)
        return ans
            
            
            
                