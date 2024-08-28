from collections import deque
class Solution(object):
    def countSubIslands(self,grid1,grid2):
        def bfs(grid,d,m):
            dhrishita=[]
            queue=deque([(d,m)])
            grid[d][m]=0  
            while queue:
                x,y=queue.popleft()
                dhrishita.append((x, y))
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==1:
                        grid[nx][ny]=0 
                        queue.append((nx,ny))
            return dhrishita
        
        def check_sub_island(island,grid1):
            for x, y in island:
                if x<0 or x>=len(grid1) or y<0 or y>=len(grid1[0]) or grid1[x][y]==0:
                    return False
            return True
        s,n=len(grid1),len(grid1[0])
        sub_islands_count=0
        
        for i in range(s):
            for j in range(n):
                if grid2[i][j] == 1:
                    island=bfs(grid2,i,j)
                    if check_sub_island(island,grid1):
                        sub_islands_count+=1
        return sub_islands_count