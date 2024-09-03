class Solution(object):
    def chalkReplacer(self, chalk, k):
        total_chalk=sum(chalk)
        k=k%total_chalk
        for d,m in enumerate(chalk):
            if k<m:
                return d
            k-=m
        
        