class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic={}
        for ind,ch in enumerate(s):
            dic[ch]=ind
            
        length=0
        ans=[]
        end=0
        for i,c in enumerate(s):
            length+=1
            if dic[c]>end:
                end=dic[c]
            if i==  end:
                ans.append(length)
                length=0
        return ans   