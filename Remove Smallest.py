n=int(input())
for i in range(n):
    leng=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    arr.sort()
    left=0
    while left<len(arr)-1:
        if abs(arr[left+1]-arr[left])<=1:
            arr.pop(left)
        else:
            left+=1
    if len(arr)==1:
        print("YES")
    else:
        print("NO")
        
    
