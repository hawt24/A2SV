class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        prev_index=0
        i=len(s)-1
        while prev_index<i:
            s[prev_index],s[i]=s[i],s[prev_index]
            prev_index+=1
            i-=1
            
        