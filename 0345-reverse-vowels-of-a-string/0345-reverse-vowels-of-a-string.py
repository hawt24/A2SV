class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=set(['a', 'e', 'i', 'o', 'u','A','E','I','O','U'])
        left=0
        right=len(s)-1
        s=list(s)
        while left<right:
            if s[left] not in vowel:
                left+=1
            elif s[right] not in vowel:
                right-=1
            else:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
        return ''.join(s)
               
            