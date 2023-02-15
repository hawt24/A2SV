class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ans=[]
        dic={}
        for i in items1:
            if i[0] not in dic:
                dic[i[0]]=i[1]
        for i in items2:
            if i[0] in dic:
                dic[i[0]]+=i[1]
            else:
                dic[i[0]]=i[1]
        for i,j in dic.items():
            ans.append([i,j])
        ans.sort()
        return ans