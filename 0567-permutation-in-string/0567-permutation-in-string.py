class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=list(s1)
        s1.sort()
        for i in range(len(s2)-len(s1)+1):
            temp=list(s2[i:i+(len(s1))])
            temp.sort()
            if temp==s1:
                return True
        return False
        
    