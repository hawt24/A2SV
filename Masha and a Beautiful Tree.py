def count_swaps(n, lis):
    res = 0
    for p in range(len(bin(n)) - 3):
        k = 2 ** p
        for q in range(0,n-1,k*2):
            if lis[q] - lis[q+k] == k:
                lis[q] -= k
                res += 1
            elif lis[q+k] - lis[q] != k:
                return -1
    return res

x = int(input())
for _ in range(x):
    a = int(input())
    b = list(map(int, input().split()))
    print(count_swaps(a, b))