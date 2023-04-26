class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        que=deque()
        visited=set()
        ans=0
        for i in range(len(isConnected)):
            if i not in visited:
                que.append(i)
                
                while que:
                    val=que.popleft()
                    visited.add(val)
                    
                    for j in range(len(isConnected)):
                        if isConnected[val][j]==1 and j not in visited:
                            que.append(j)
                ans+=1
        return ans