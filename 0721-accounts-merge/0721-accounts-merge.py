class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph=defaultdict(list)
        parent=defaultdict(list)
        
        for item in accounts:
            name=item[0]
            for j in item[1:]:
                graph[j]=name
                parent[j]=j
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
                
            return parent[x]

        
        def union(email1,email2):
            x,y=find(email1),find(email2)
            if x!=y:
                parent[y]=x
      
        for item in accounts:
            email1=item[1]
            for email2 in item[2:]:
                union(email1,email2)
                
        ans=[]
        grup=defaultdict(list)
        for email in parent:
            result=find(email)
            grup[result].append(email)
        
        
        for item in grup:
            ans.append([graph[item]]+sorted(grup[item]))
        return ans
            
        
            
    
                
        
            
    

    