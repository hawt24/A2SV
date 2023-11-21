class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        graph = defaultdict(dict)

        # Build the graph
        for (numerator, denominator), value in zip(equations, values):
            graph[numerator][denominator] = value
            graph[denominator][numerator] = 1 / value

        def dfs(start, target, visited):

            if start not in graph or target not in graph:
                return -1.0
         
            if start == target:
                return 1.0

            visited.add(start)
            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, target, visited)
                    if result != -1.0:
                        return value * result

            return -1.0

        ans = []
        for query in queries:
            start, target = query
            ans.append(dfs(start, target, set()))

        return ans