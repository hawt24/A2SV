class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        stack=[]
        visited=set()
        ans=0
        for i in range(len(isConnected)):
            if i not in visited:
                stack.append(i)
                
                while stack:
                    val=stack.pop()
                    visited.add(val)
                    
                    for j in range(len(isConnected)):
                        if isConnected[val][j]==1 and j not in visited:
                            stack.append(j)
                ans+=1
        return ans