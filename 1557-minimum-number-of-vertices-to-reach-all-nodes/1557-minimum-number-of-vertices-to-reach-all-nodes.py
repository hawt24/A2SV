class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans=[]
        graph=defaultdict(int)
        for i ,j in edges:
            graph[j] = 1
        for i in range(n):
            if graph[i]==0:
                ans.append(i)
        return list(set(ans))
            
