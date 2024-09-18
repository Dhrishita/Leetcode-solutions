from functools import cmp_to_key
class Solution(object):
    def largestNumber(self,nums):
        num_str=list(map(str,nums))
        def compare(D,M):
            if D+M>M+D:
                return -1  
            elif D+M<M+D:
                return 1  
            else:
                return 0 
        num_str.sort(key=cmp_to_key(compare))
        largest=''.join(num_str)
        return '0' if largest[0] == '0' else largest