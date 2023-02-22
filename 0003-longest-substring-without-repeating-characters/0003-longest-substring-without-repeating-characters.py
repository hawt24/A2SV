class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_=set()
        left=0
        ans=0
        for i in range(len(s)):
            while s[i] in set_:
                set_.remove(s[left])
                left+=1
            set_.add(s[i])
            ans=max(ans,i-left+1)
        return ans
            
                
        
        

        
                
                
            