class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        s = list(s)
        ans = 0
        dic = Counter()
        
        for right in range(len(s)):
            dic[s[right]] += 1
            length = right - left + 1
            
            while length - max(dic.values()) > k:
                dic[s[left]] -= 1
                length -= 1
                left += 1
                
            ans = max(ans, length)
            
        return ans
                
                
