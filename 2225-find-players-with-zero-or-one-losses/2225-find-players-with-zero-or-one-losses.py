class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss=Counter()
        player=set()
        for winner,losser in matches:
            loss[losser]+=1
            player.add(winner)
            player.add(losser)
        
        one_loss=[]
        not_lost=[]
        for i in player:
            if loss[i]==0:
                not_lost.append(i)
            elif loss[i]==1:
                one_loss.append(i)
        return [sorted(not_lost),sorted(one_loss)]
    
                
                
            
            
     