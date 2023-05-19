class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        heap=[(0,0)]
        
        dic=defaultdict(list)
        for i in range(len(points)):
            x1,y1=points[i]
            for j in range(i+1,len(points)):
                x2,y2=points[j]

                temp=abs(x1-x2)+abs(y1-y2)
                dic[i].append((temp,j))
                dic[j].append((temp,i))
                
        visited=set()
        ans=0
        
        while len(visited)<len(points):
            dist,index=heappop(heap)
            if index in visited:
                continue
            ans+=dist
            visited.add(index)
            
            for nigh_dist,nigh_index in dic[index]:
                if nigh_index not in visited:
                    heappush(heap,(nigh_dist,nigh_index))
                    
        return ans
            
            
            
        
        
        