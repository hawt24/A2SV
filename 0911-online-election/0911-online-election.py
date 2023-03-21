class TopVotedCandidate:
    def __init__(self, persons, times):
        self.winnerlist = []
        self.timelist = []
        a = dict()
        winner = persons[0]
        a[winner] = 1
        self.winnerlist.append(winner)
        self.timelist.append(times[0])
        for i in range(1, len(times)):
            if persons[i] not in a:
                a[persons[i]] = 1
            else:
                a[persons[i]] += 1
                
            if a[persons[i]] >= a[winner]:
                if (persons[i] != winner):
                    winner = persons[i]
                    self.winnerlist.append(winner)
                    self.timelist.append(times[i])
    def q(self, t):
        num = bisect.bisect_right(self.timelist, t)
        return self.winnerlist[num - 1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)