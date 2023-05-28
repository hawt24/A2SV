class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def dp(i, j):
            if i == 0:
                return True
            if j == 0:
                return False
            if s[i-1] == t[j-1]:
                return dp(i-1, j-1)
            else:
                return dp(i, j-1)
        
        return dp(len(s), len(t))
        