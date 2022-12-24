class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left=0
        right=0
        ans=""
        while left<len(word1) and right<len(word2):
            ans+=word1[left]+word2[right]
            left+=1
            right+=1
        return ans+word1[left:]+word2[right:]
            
            