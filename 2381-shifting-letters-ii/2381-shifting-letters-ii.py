class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        summ=[0]*(len(s)+1)
        ans=""
        for start,end, direction in shifts:
            if direction==1:
                summ[start]+=1
                summ[end+1]-=1
            else:
                summ[start]-=1
                summ[end+1]+=1
    
        for i in range(1,len(s)):
            summ[i]+=summ[i-1]
        for idx in range(len(s)):
            ans+= chr((ord(s[idx]) - ord('a') + summ[idx]) % 26 + ord('a'))
        
        return ans
        
        
        