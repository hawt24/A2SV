from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        
        graph = defaultdict(list)
        for i in range(0,n+1):
            graph[i]=[]
        for x, y in edges:
            graph[y].append(x)
    
            
            
        def dfs(node,ansistor):
            stack=[node]
            while stack:
                curr=stack.pop()
                for nigh in graph[curr]:
                    if nigh not in ansistor:
                        ansistor.add(nigh)
                        stack.append(nigh)
                        dfs(node,ansistor)
                
        ans=[]
        for i in range(n):
            ansistor=set()
            dfs(i,ansistor)
            
            if ansistor:
                ans.append(sorted(list(ansistor)))
            else:
                ans.append([])
        return ans
            
                
            
        
            
        
