class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph=defaultdict(list)
        prob=defaultdict(list)
        for index,(u,v)  in enumerate(edges):
            graph[u].append(v)
            graph[v].append(u)
            prob[(u,v)] = succProb[index]
            prob[(v,u)] = succProb[index]
            
        dist=[float("-inf") for i in range(n)]
        dist[start_node]=1
        
        
            
        heap=[]
        heap.append((start_node,1))
        
        while heap:
            
            par,dis=heap.pop()
            children=graph[par]
            for nigh in children:
                new_dist=dis*prob[(nigh,par)]
                
                if new_dist>dist[nigh]:
                    heappush(heap,(nigh,new_dist))
                    dist[nigh]=new_dist
    

                    
        if dist and dist[end_node] != float("-inf"):
            return dist[end_node] 
        else:
            return 0
            
        
        

      
            
                
            
            
        
      
    
        