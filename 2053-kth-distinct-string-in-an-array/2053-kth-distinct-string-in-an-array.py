class Solution(object):
    def kthDistinct(self, arr, k):
        cnt=collections.Counter(arr)
        for d in arr:
            if cnt[d]==1:
                k-=1
                if k==0:
                    return d
        return ''
        
        