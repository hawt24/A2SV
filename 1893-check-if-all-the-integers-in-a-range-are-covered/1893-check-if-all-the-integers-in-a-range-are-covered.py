class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        posiblity=[]
        for i in range(left,right+1):
            posiblity.append(i)
        for i in ranges:
            for j in range(i[0],i[1]+1):
                if j in posiblity:
                    posiblity.remove(j)
        return len(posiblity)==0
            
        