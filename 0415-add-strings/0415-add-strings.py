class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # digits_integer1 = int(''.join(map(str,num1)))
        # digits_integer2 = int(''.join(map(str,num2)))
        # return str(digits_integer1+digits_integer2)
        return str(sum(list(map(int,[num1,num2]))))