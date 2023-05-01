from sortedcontainers import SortedList
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        temp=SortedList([])
        ans=[]
        for i in range(len(arr)):
            temp.add(((bin(arr[i]).count("1")),arr[i]))
        for i,j in temp:
            ans.append(j)
        return ans


     
        