n,m=list(map(int,input().split()))
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
st_1=0
st_2=0
ans=[]
while st_1<len(arr1) and st_2<len(arr2):
    if arr1[st_1]<arr2[st_2]:
        ans.append(arr1[st_1])
        st_1+=1
    else:
        ans.append(arr2[st_2])
        st_2+=1
if st_1<len(arr1):
    for i in range(st_1,len(arr1)):
        ans.append(arr1[i])
        st_1+=1
else:
    for i in range(st_2,len(arr2)):
        ans.append(arr2[i])
        st_2+=1
print(" ".join(map(str,ans)))
