class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = []
        nums = sorted(zip(position, speed), reverse=True)
        
        for x, y in nums:
            stack.append((target-x) / y)
        
        ans, prev = 0, 0
        for i in range(n):
            if stack[i] > prev:
                ans += 1
                prev = stack[i]
        
        return ans