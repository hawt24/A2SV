class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        s=list(s)
        stack=[]
        cnt=Counter(s)
        cheak=set()
        
        for i in range(len(s)):
            cnt[s[i]] -= 1
            while stack and s[i] < stack[-1] and cnt[stack[-1]] > 0 and s[i] not in cheak:
                cheak.remove(stack.pop())
            
            if s[i] not in cheak:
                cheak.add(s[i])
                stack.append(s[i])
                
        return "".join(stack)
            
        
        
    
            
       
        
            
                