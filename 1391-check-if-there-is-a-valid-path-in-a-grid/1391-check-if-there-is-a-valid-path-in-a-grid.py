class UnionFind:
    def __init__(self, n):
        self.graph=list(range(n))
        self.rank=[1]*n
    def find(self,x):
        if self.graph[x]!=x:
            path = []
            while x != self.graph[x]:
                path.append(x)
                x = self.graph[x]
            for p in path:
                self.graph[p] = x
        return self.graph[x]
    def union(self,x,y):
        xrep,yrep=self.find(x),self.find(y)
        
        if xrep==yrep:
            return
        if self.rank[xrep]<self.rank[yrep]:
            self.graph[xrep]=yrep
        elif self.rank[yrep]<self.rank[xrep]:
            self.graph[yrep]=xrep
        else:
            self.graph[xrep]=yrep
            self.rank[yrep]+=self.rank[xrep]
    
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        move={1:[(0,1), (0,-1)],2:[(1,0), (-1,0)],3:[(1,0), (0,-1)],4:[(1,0), (0,1)],5:[(-1,0), (0,-1)],6:[(-1,0), (0,1)]}
        def is_valid(pos):
            x, y = pos
            return  0<=x<len(grid) and 0<=y<len(grid[0])
            
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] in move:
                    for x, y in move[grid[i][j]]:
                        nr, nc = i + x, j + y
                        if is_valid((nr,nc)) and (-x, -y) in move[grid[nr][nc]]:
                            uf.union(i*n+j, nr*n+nc)
        return uf.find(0)==uf.find(m*n-1)