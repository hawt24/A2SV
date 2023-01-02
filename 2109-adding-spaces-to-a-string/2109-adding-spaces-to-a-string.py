class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        string=''
        spaces=set(spaces)
        for i in range(len(s)):
            if i in spaces:
                string+=" "+s[i]
            else:
                string+=s[i]
        return string
                
      