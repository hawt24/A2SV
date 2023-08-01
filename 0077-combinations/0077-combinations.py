class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start, path):
            #base case
            if len(path) == k:
                answer.append(path)
                return
            for i in range(start+1, n + 1):
                backtrack(i, path + [i])
              
        answer = []

        backtrack(0, [])
        return answer
        