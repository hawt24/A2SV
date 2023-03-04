class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(1, rowIndex+ 2):
            row = [1] * i
            for j in range(1,i-1):
                row[j] = ans[i - 2][j] + ans[i - 2][j - 1]
            ans.append(row)
        return ans[rowIndex]