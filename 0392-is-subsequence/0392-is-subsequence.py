class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        ptr_1=0
        ptr_2=0
        while ptr_1<len(s) and ptr_2< len(t):
            if s[ptr_1]==t[ptr_2]:
                ptr_1+=1
                ptr_2+=1
            else:
                ptr_2+=1
        return ptr_1==len(s)
            
        