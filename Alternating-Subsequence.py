test_case=int(input())
for _ in range(test_case):
    n=int(input())
    nums=list(map(int,input().split()))
    right = 0
    if nums[0]>0:
        flag=1
    else:
        flag=0
    summ = 0
    key = nums[0]
    while right < len(nums):
        if flag == 1 and nums[right] > 0:
            key = max(key, nums[right])
            right += 1
        elif flag == 1 and nums[right] < 0:
            summ += key
            key = nums[right]
            right += 1
            flag = 0
        elif flag == 0 and nums[right] < 0:
            key = max(key, nums[right])
            right += 1
        elif flag == 0 and nums[right] > 0:
            summ += key
            key = nums[right]
            right += 1
            flag = 1
    summ += key
    print(summ)

    