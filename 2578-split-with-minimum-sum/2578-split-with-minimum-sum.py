class Solution:
    def splitNum(self, num: int) -> int:
        num1=""
        num2=""
        arr=[int(i) for i in str(num)]
        arr.sort()
        for i in range(len(arr)):
            if i%2==0:
                num1+=str(arr[i])
            else:
                num2+=str(arr[i])
        return int(num1)+int(num2)