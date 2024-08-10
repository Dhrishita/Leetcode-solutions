class Solution(object):
    def regionsBySlashes(self, grid):
        n=len(grid)
        # Create a 3n x 3n grid for tracking regions
        expanded_grid=[[0]*(3*n) for _ in range(3*n)]
        
        # Fill the expanded grid based on the original grid
        for i in range(n):
            for j in range(n):
                if grid[i][j]=='/':
                    expanded_grid[i*3][j*3+2]=1
                    expanded_grid[i*3+1][j*3+1]=1
                    expanded_grid[i*3+2][j*3]=1
                elif grid[i][j]=='\\':
                    expanded_grid[i*3][j*3]=1
                    expanded_grid[i*3+1][j*3+1]=1
                    expanded_grid[i*3+2][j*3+2]=1
        
        # Applying DFS
        def dfs(x,y):
            if x<0 or x>=3*n or y<0 or y>=3*n or expanded_grid[x][y]==1:
                return
            expanded_grid[x][y]=1
            # Visit all 4 directions
            dfs(x-1,y)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x,y+1)

        # Count the number of regions
        regions=0
        for i in range(3*n):
            for j in range(3*n):
                if expanded_grid[i][j]==0:
                    dfs(i,j)
                    regions+=1
        return regions