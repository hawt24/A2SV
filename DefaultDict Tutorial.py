from collections import defaultdict
dict=defaultdict(list)
list1=[]
m,n=map(int,input().split())
for i in range(m):
    a=input()
    dict[a].append(i+1)
for i in range(n):
    b=input()
    list1=list1+[b]
for i in list1:
    if i in dict:
        print(' '.join(map(str,dict[i])))
    else:
        print("-1")
