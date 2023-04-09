class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck)==1:
            return False
        cnt=Counter(deck)
        values = cnt.values()
        x= math.gcd(*values)
        if x>= 2:
            return True 
        else:
            return False
        