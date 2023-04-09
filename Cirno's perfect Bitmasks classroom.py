test_case=int(input())
for i in range(test_case):
    n=int(input())
    y = 1
    if n == 1:
        print(3)
        continue
    i = 1
    while i > 0 and not(n & y):
        y <<= 1

    if n == y:
        print(y+1)
    else:
        print(y)
   