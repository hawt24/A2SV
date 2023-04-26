from collections import defaultdict
n = int(input())
mat=[]
ans=[]
visited=set()
for i in range(n):
    mat.append(list(map(int, input().split())))
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==1 and (i,j) not in visited:
                visited.add((i,j))
                ans.append([i,j+1])
graph=defaultdict(list)
for i,j in ans:
    graph[i].append(j)
for key,val in graph.items():
    print(len(val),*val)
