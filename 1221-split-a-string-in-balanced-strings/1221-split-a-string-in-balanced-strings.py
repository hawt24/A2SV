class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count_R = 0
        count_L = 0
        ans = 0
        for i in s:
            if i == 'R': count_R += 1
            else: count_L += 1
            if count_R == count_L:
                ans += 1
                count_R = 0
                count_L = 0
        return ans 
        