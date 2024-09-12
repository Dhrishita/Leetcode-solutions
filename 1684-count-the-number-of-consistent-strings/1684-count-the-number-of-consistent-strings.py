class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed_set=set(allowed)
        cnt=0
        for word in words:
            if all(char in allowed_set for char in word):
                cnt+=1
        return cnt
    
        