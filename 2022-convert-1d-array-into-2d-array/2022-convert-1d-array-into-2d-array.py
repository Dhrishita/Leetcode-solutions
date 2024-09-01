class Solution(object):
    def construct2DArray(self, original, m, n):
        if len(original)!=m*n:
            return []
        dhrishita=[]
        for i in range(0,len(original),n):
            dhrishita.append(original[i:i+n])
        return dhrishita