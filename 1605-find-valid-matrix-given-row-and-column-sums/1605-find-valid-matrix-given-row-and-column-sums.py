class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        d=len(rowSum)
        m=len(colSum)
        matrix=[[0]*m for _ in range(d)]
        for i in range (d):
            for j in range(m):
                min_of_both=min(rowSum[i],colSum[j])
                matrix[i][j]=min_of_both
                rowSum[i]-=min_of_both
                colSum[j]-=min_of_both
        
        return matrix