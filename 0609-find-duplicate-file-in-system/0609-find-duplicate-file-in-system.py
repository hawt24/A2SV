class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for i in paths:
            i=i.split(" ")
            name=i[0]
            for j in i[1:]:
                j=j.split(".txt")
                name_=j[0]
                content=j[1]
                dic[content].append((name,name_))
                
        ans=[]
        for key,val in dic.items():
            if len(val)>1:
                temp=[]
                for x, y in val:
                    temp.append(x+'/'+y+'.txt')
                ans.append(temp)
        return ans
        
        