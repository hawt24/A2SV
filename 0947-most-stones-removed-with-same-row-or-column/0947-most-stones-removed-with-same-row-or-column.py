class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
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
                
        for u in range(len(stones)):
            temp=stones[u]
            for v in range(len(stones)):
                curr=stones[v]
                if temp[0]==curr[0] or temp[1]==curr[1]:
                    union(u,v)
            
        ans=len(stones)
        for i in graph:
            if i==graph[i]:
                ans-=1
        return ans
    
                
                
                
                
    
            
        
        
        