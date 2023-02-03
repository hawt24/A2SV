class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        dic={row:"" for row in range(1,numRows+1)}
        row=1
        up=True
        for lett in s:
            dic[row]+=lett
            if row ==1 or(row<numRows and up):
                row+=1
                up=True
            else:
                up=False
                row-=1
        ans=""
        for i in range(1,numRows+1):
            ans+=dic[i]
        return ans
      