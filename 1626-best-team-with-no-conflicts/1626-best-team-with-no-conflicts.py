class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        
        Sorted_list=sorted(list(zip(ages, scores)))
        max_scores=[0]*(len(scores))
        max_scores[0]=Sorted_list[0][1]
        
        for i in range(1,len(Sorted_list)):
            max_scores[i]=Sorted_list[i][1]
            
            for j in range(i):
                if Sorted_list[j][1]<=Sorted_list[i][1]:
                    
                    max_scores[i]=max(max_scores[i],Sorted_list[i][1]+max_scores[j])
                    
        return max(max_scores)
        