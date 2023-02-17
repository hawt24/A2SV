class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1=set("qwertyuiop")
        set2=set("asdfghjkl")
        set3=set("zxcvbnm")
        ans=[]
        for i in words:
            temp=set(i.lower())
            if temp.issubset(set1) or temp.issubset(set3) or temp.issubset(set2):
                ans.append(i)
        return ans
        
        