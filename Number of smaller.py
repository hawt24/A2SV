n,m=list(map(int,input().split()))
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
st=0
for i in range(len(arr2)):
  
    while st<len(arr1) and arr2[i]>arr1[st]:
        st+=1
    print(st,end=" ")
