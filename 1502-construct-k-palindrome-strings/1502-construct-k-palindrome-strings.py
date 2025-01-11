from collections import Counter
class Solution(object):
    def canConstruct(self, s, k):
        dhrishita=Counter(s)
        odd_cnt=sum(1 for cnt in dhrishita.values() if cnt%2!=0)
        return odd_cnt<=k<=len(s)    