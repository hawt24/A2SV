class Solution:
    def printVertically(self, s: str) -> List[str]:
        s=s.split()
        max_len=0
        answer=[]
        for i in s:
            if len(i)>max_len:
                max_len=len(i)
        for i in range(max_len):
            ans=[]
            for j in range(len(s)):
                if len(s[j])>i:
                    ans.append(s[j][i])
                else:
                    ans.append(" ")
            
                    
            answer.append(ans)

        final_ans=[]
        for ans in answer:
            final_ans.append(''.join(ans).rstrip())
        return final_ans
        
            
            
                    
                
            
            
            