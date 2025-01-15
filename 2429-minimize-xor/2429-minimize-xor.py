class Solution(object):
    def minimizeXor(self, num1, num2):
        D=bin(num2).count('1')
        x=0
        for m in range(31, -1, -1):
            if D>0 and (num1&(1<<m)):
                x|=(1<<m)
                D-=1
        
        for m in range(32):
            if D>0 and not (x&(1<<m)):
                x|=(1<<m)
                D-=1
        return x