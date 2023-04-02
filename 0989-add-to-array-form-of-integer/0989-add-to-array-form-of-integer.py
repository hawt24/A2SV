class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        digits_integer = int(''.join(map(str,num)))
        digits_integer+=k
        return list(map(int,str(digits_integer)))