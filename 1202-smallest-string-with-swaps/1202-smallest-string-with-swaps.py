class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = defaultdict(list)
        for x, y in pairs:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = set()
        components = []
        
        def dfs(node, component):
            visited.add(node)
            component.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)
    
        for i in range(len(s)):
            if i not in visited:
                component = []
                dfs(i, component)
                components.append(component)
        
        for component in components:
            component.sort()
            chars = [s[i] for i in component]
            chars.sort()
            for i, j in enumerate(component):
                s = s[:j] + chars[i] + s[j+1:]
        
        return s