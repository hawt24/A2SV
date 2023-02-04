class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s1.sort()
        len_s1 = len(s1)
        for i in range(len(s2)-len_s1+1):
            temp= list(s2[i:i+len_s1])
            temp.sort()
            if temp== s1:
                return True
        return False   
