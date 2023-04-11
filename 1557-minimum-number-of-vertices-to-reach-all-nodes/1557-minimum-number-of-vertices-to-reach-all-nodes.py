class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        temp=set()
        ans=[]
        graph=defaultdict(list)
        for i ,j in edges:
            temp.add(j)
        for i,j in edges:
            if i not in temp:
                ans.append(i)
        return list(set(ans))
            
