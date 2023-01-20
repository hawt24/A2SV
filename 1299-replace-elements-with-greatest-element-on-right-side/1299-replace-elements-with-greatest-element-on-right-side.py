class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val=-1
        for i in range(len(arr)-1,-1,-1):
            maxm=max(max_val,arr[i])
            arr[i]=max_val
            max_val=maxm
        return arr
    