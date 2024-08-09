class Solution(object):
    def magic_square(self, grid,r,c):
            nums={grid[r+i][c+j] for i in range(3) for j in range(3)}
            if nums!={1, 2, 3, 4, 5, 6, 7, 8, 9}:
                return False
            sum_of_1_row=sum(grid[r][c:c+3])
                
            if sum(grid[r+1][c:c+3])!=sum_of_1_row or sum(grid[r+2][c:c+3])!=sum_of_1_row:
                return False
                
            if sum(grid[r+i][c] for i in range(3))!=sum_of_1_row or sum(grid[r+i][c+1] for i in range(3))!=sum_of_1_row or sum(grid[r+i][c+2] for i in range(3))!=sum_of_1_row:
                return False
                
            if grid[r][c]+grid[r+1][c+1]+grid[r+2][c+2]!=sum_of_1_row:
                return False
                
            if grid[r][c+2]+grid[r+1][c+1]+grid[r+2][c]!=sum_of_1_row:
                return False
            return True
            
    def numMagicSquaresInside(self,grid):
        row=len(grid)
        col=len(grid[0])
        if row<3 or col<3:
            return 0
        
        cnt=0
        for r in range(row-2):
            for c in range(col-2):
                if self.magic_square(grid,r,c):
                    cnt+=1
        return cnt        