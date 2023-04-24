class Solution:
    def reverseBits(self, n: int) -> int:
        # zfill is used to add zeros at the begining of the string until it reaches the length as              specidifed
        temp=bin(n)[2:]
        temp=temp.zfill(32)
        return int(temp[::-1],2)