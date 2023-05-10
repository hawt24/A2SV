class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """"
        # Color codes:
        # white: not visited yet
        # gray: visiting (in recursion stack)
        # black: visited (safe)"""
        
        white, gray, black = 0, 1, 2
        def dfs(node):
            if colors[node] != white:
                return colors[node] == black
            colors[node] = gray
            for neighbor in graph[node]:
                if colors[neighbor] == black:
                    continue
                if colors[neighbor] == gray or not dfs(neighbor):
                    return False
            colors[node] = black
            return True
        n = len(graph)
        colors = [white] * n
        ans=[i for i in range(n) if dfs(i)]
        return sorted(ans)