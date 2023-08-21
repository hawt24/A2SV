class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        dic={"++X":1,"X++":1,"--X":-1,"X--":-1}
        ans=0
        for i in operations:
            if i in dic:
                ans+=dic[i]
        return ans
        