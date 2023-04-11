n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))
row=[]
col=[]
temp=0
temp1=0
for i in range(len(mat)):
    x=sum(mat[i])
    row.append(x)

for j in range(len(mat[0])):
    t=0
    for i in mat:
        t+=i[j]
    col.append(t)

ans1=[]
for i in range(len(col)):
    if col[i]==0:
        ans1.append(i+1)
print(len(ans1),*ans1)
ans2=[]
for i in range(len(row)):
    if row[i]==0:
        ans2.append(i+1)
print(len(ans2),*ans2)