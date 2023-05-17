class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited=set()
        graph=defaultdict(int)
        def find(x):
            if x not in graph:
                graph[x]=x
                
            while graph[x]!=x:
                graph[x]=graph[graph[x]]
                x=graph[x]
                
            return x
        
        
        for x,y in edges:
            p1,p2=find(x),find(y)
            if p1 not in visited or p2 not in visited or p1!=p2:
                visited.add(p1)
                visited.add(p2)
                graph[p1]=p2
            else:
                return [x,y]
