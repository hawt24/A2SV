n = int(input())
ans=0
for i in range(n):
    mat=list(map(int,input().split()))
    for i in range(len(mat)):
        if mat[i]==1:
            ans += 1
print(ans//2)