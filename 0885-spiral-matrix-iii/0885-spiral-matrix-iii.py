class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        result=[]
        directions=[(0,1),(1,0),(0,-1),(-1,0)]  
        index=0
        steps=1
        r,c=rStart,cStart

        while len(result)<rows*cols:
            for _ in range(2):
                for _ in range(steps):
                    if 0<=r<rows and 0<=c<cols:
                        result.append([r,c])
                    r+=directions[index][0]
                    c+=directions[index][1]
                
                index=(index+1)%4
            steps+=1
        return result
