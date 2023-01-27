class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        st_1=0
        st_2=0
        count=0

        while st_1<len(players) and st_2<len(trainers):
            if players[st_1]<=trainers[st_2]:
                count+=1
                st_1+=1
                st_2+=1
            else:
                st_2+=1
            
        return count
            
                
                