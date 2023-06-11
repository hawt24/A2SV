class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        dic= {}
        for index,item in enumerate(score):
            dic[item[k]] = index                     
        sort_key = sorted(dic.keys(),reverse=True)   
        ans= []
        for key in sort_key:
            ans.append(score[dic[key]])           
        return ans