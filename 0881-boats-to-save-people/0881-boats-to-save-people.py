class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats=0
        people.sort()
        light,heavy=0,len(people)-1
        while light<=heavy:
            remain=limit-people[heavy]
            heavy-=1
            boats+=1
            if light<=heavy and remain>=people[light]:
                light+=1
        return boats
        
        