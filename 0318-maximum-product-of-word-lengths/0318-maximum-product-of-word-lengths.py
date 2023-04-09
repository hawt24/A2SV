class Solution:
    def maxProduct(self, words: List[str]) -> int:
        """
         create a new array to contain binary representation of the words.
        (&) for word1 and word2 is 0, then there is no common chars between them."""
        l = len(words)
        bitmasks = [0]*l
        for i in range(l):
            for c in words[i]:
                bitmasks[i] |= 1 << (ord(c) - ord('a'))
                
        ans=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if bitmasks[i]& bitmasks[j]==0:
                    ans=max(ans,len(words[i])*len(words[j]))
        return ans
        
     