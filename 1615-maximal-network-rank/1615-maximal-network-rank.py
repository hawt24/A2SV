class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph=defaultdict(list)
        for sorce,dest in roads:
            graph[sorce].append(dest)
            graph[dest].append(sorce)
            
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                curr=len(graph[i])+len(graph[j])
                if j in graph[i]:
                    curr -= 1
                ans=max(ans,curr)
        
        return ans
        