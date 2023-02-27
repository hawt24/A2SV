class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque([(num, i) for i, num in enumerate(tickets)])
        seconds = 0
        while True:
            num, index = queue.popleft()
            if index == k and num <= 1:
                return seconds+1
            if num > 1:
                queue.append((num-1, index))
            seconds += 1
        return seconds