class Solution(object):
    def minimumDeletions(self, s):
        cnt=0
        min_deletions=0
        
        for char in s:
            if char=='b':
                cnt+=1
            else:
                min_deletions=min(min_deletions+1,cnt)
        return min_deletions
                
        