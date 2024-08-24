class Solution(object):
    def nearestPalindromic(self, n):
        def create_palindromes(prefix, length):
            if length%2==0:
                return str(prefix)+str(prefix)[::-1]
            else:
                return str(prefix)+str(prefix)[:-1][::-1]

        length=len(n)
        num=int(n)
        D=set()

        D.add(10**(length-1)-1) 
        D.add(10**length+1)        

        prefix=int(n[:(length+1)//2]) 
        for diff in [-1,0,1]:
            new_prefix=prefix+diff
            D.add(int(create_palindromes(new_prefix, length)))
        D.discard(num)

        closest_pal=None
        min_diff=float('inf')

        for M in D:
            diff = abs(M-num)
            if diff<min_diff or (diff==min_diff and M<closest_pal):
                closest_pal=M
                min_diff=diff
        return str(closest_pal)