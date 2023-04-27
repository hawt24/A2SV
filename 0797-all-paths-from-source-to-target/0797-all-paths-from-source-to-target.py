class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        last_node=len(graph)-1
        
        def dfs(node,path,ans):
            
            if node==last_node:
                ans.append(path)
                
            for nigh in graph[node]:
                
                dfs(nigh,path+[nigh],ans)
                
                
        ans=[]
        dfs(0,[0],ans)
        return ans