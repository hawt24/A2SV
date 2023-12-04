class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        else:
            prev_triangle = self.generate(numRows - 1)
            last_row = prev_triangle[-1]
            
            current_row = [1]
            for i in range(1, numRows - 1):
                current_row.append(last_row[i - 1] + last_row[i])
                
            current_row.append(1)
            prev_triangle.append(current_row)
            
            return prev_triangle
