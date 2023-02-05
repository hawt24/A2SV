class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_count=Counter(s[:len(p)-1])
        p_count=Counter(p)
        start=0
        ans=[]
        for i in range(len(p)-1,len(s)):
            s_count[s[i]]+=1
            if s_count==p_count:
                ans.append(start)
            s_count[s[start]]-=1
            start+=1
        return ans
                
                
        
            
    