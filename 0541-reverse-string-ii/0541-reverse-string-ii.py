class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans=[]
        flag=True
        for i in range(0,len(s),k):
            reverse=s[i:i+k]
            if flag:
                ans.append(reverse[: :-1])
            else:
                ans.append(reverse)
            flag=not flag
        return "".join(ans)
                
            
            
        
            
            
  
    
            