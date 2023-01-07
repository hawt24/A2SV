class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans=[]
        res=[]
        temp=""
        for i in range(len(source)):
            word=list(source[i])
            for j in range(len(word)):
                if j<len(word)-1 and (word[j]+word[j+1])=="/*" and len(res)==0:
                    res.append([i,j+1])
                elif (word[j-1]+word[j])=="*/" and res and res[-1]!=[i,j-1]:
                    res.pop()
                elif j<len(word)-1 and (word[j]+word[j+1])=="//" and len(res)==0:
                    if temp:
                        ans.append(temp)
                    temp=""
                    break
                elif len(res)==0:
                    temp+=word[j]
            if len(res)==0 and temp:
                ans.append(temp)
                temp=""
        return ans
                