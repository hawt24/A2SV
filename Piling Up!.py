def func(bloks):
    left=0
    right=len(bloks)-1
    compare=float("inf")
    while left<=right:
       if bloks[left]>=bloks[right] and bloks[left]<=compare:
        compare=bloks[left]
        left+=1
       elif bloks[left]<bloks[right] and bloks[right]<=compare:
        compare=bloks[right]
        right-=1 
       else:
        return "No"
    return "Yes"
         
test_case=int(input())
for i in range(test_case):
    n=int(input())
    bloks=[int(x) for x in input().split()]
    print(func(bloks))
    
    
