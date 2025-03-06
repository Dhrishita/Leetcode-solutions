class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        d=len(grid)
        cnt={}
        for row in grid:
            for num in row:
                cnt[num]=cnt.get(num,0)+1
        r=-1
        m=-1
        for i in range(1,d*d+1):
            if i in cnt:
                if cnt[i]==2:
                    r=i
            else:
                m=i
        return [r,m]