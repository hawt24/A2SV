class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        cnt=defaultdict(int)
        ing=defaultdict(list)
        
        supplies=set(supplies)
        que=deque()
        
        for i in range(len(recipes)):
            for j in ingredients[i]:
                
                if j not in supplies:
                    ing[j].append(recipes[i])
                    cnt[recipes[i]]+=1

            if cnt[recipes[i]]==0:
                que.append(recipes[i])
            
        ans=[]           
        while que:
            curr=que.popleft()
            ans.append(curr)
            
            for nigh in ing[curr]:
                cnt[nigh]-=1
                if cnt[nigh]==0:
                    que.append(nigh)
        return ans
            
            
            
            
                    
                
            
       