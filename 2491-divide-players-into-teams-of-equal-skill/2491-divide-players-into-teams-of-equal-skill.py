class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left=0
        right=len(skill)-1
        total=0
        temp=skill[0]+skill[-1]
        while left<right:
            if skill[left]+skill[right]==temp:
                total+=skill[right]*skill[left]
                left+=1
                right-=1
            else:
                return -1
        return total
                

        