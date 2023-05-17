class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
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
        for x,y in zip(s1,s2):
            union(x,y)
        ans=""   
        for i in baseStr:
            ans+=find(i)
        return ans
                