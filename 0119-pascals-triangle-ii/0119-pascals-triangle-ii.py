class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        nrow = 1
        while nrow <= rowIndex+1:
            newRow = [1] * nrow
            for i in range(1,nrow-1):
                newRow[i] = row[i-1] + row[i]
            row = newRow
            nrow += 1
        return newRow
