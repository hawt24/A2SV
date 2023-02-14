class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans=[]
        arr.sort()
        min_=[]
        for i in range(len(arr)-1):
            min_.append(arr[i+1]-arr[i])

        min_arr=min(min_)

        for j in range(len(arr)-1):
            if (arr[j+1]-arr[j])==min_arr:
                ans.append([arr[j],arr[j+1]])
        return ans