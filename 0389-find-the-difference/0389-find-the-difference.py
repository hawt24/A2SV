class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        list1=list(s)
        list2=list(t)
        for i in list1:
            list2.remove(i)
        return list2[0]
       
    
       