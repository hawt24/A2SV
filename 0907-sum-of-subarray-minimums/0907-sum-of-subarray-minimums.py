class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.append(0)
        stack=[-1]
        ans=0
        for i in range(len(arr)):
            while arr[i]<arr[stack[-1]]:
                index=stack.pop()
                ans+=arr[index]*(i-index)*(index-stack[-1])
            stack.append(i)
        return ans%(10**9+7)