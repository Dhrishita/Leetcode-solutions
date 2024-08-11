class Solution(object):
    def minDays(self, grid):
        def bfs(i,j,visited):
            queue=deque([(i,j)])
            visited.add((i,j))
            directions=[(0, 1),(1, 0),(0, -1),(-1, 0)]
            while queue:
                x,y=queue.popleft()
                for dx, dy in directions:
                    mx,my=x+dx,y+dy
                    if 0<=mx<len(grid) and 0<=my<len(grid[0]) and grid[mx][my]==1 and (mx,my) not in visited:
                        visited.add((mx,my))
                        queue.append((mx,my))

        def isConnected():
            visited=set()
            found_island=False
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j]==1 and (i,j) not in visited:
                        if found_island:  
                            return False
                        bfs(i,j,visited)
                        found_island=True
            return found_island
        
        if not isConnected():
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    grid[i][j]=0
                    if not isConnected():
                        return 1
                    grid[i][j]=1  
        return 2