class Solution:
    def reverseWords(self, s: str) -> str:
        ans=""
        left=0
        right=0
        while right<=len(s):
            if len(s)== right:
                ans+=(s[left:right][::-1])
            elif s[right]==" ":
                ans+=(s[left:right][::-1])+" "
                left=right+1
            right+=1
        return ans
                
            
                
      