class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ans=0
        for i in moves:
            if i=="R":
                i=1
            elif i=="L":
                i=-1
            elif i=="U":
                i=5
            elif i=="D":
                i=-5
            ans+=i
        return True if ans==0 else False
        