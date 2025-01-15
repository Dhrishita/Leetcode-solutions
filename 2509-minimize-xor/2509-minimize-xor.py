class Solution(object):
    def minimizeXor(self, num1, num2):
        k = bin(num2).count('1')
        x = 0
        for i in range(31, -1, -1):
            if k > 0 and (num1 & (1 << i)):
                x |= (1 << i)
                k -= 1
        
        for i in range(32):
            if k > 0 and not (x & (1 << i)):
                x |= (1 << i)
                k -= 1
        return x