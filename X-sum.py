from collections import defaultdict
ans=[]
test_case=int(input())
for i in range(test_case):
    diagonals = defaultdict(int)
    antiDiagonals = defaultdict(int)
    n,m=list(map(int,input().split()))
    mat = [[0]*m for i in range(n)]
    for rowIndex in range(n):
 
        row= list(map(int, input().split()))
 
        for columnIndex in range(m):
            mat[rowIndex][columnIndex] = row[columnIndex]
            diagonals[rowIndex-columnIndex] += row[columnIndex]
            antiDiagonals[rowIndex + columnIndex] += row[columnIndex]
    max_ = 0
    for rowIndex in range(n):
        for columnIndex in range(m):
            summ = diagonals[rowIndex-columnIndex] + antiDiagonals[rowIndex + columnIndex] - mat[rowIndex][columnIndex]
            max_ = max(max_, summ )
    ans.append(max_)
for i in ans:
    print(i)
 