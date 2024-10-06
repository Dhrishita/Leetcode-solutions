from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        len_s1,len_s2=len(s1),len(s2)
        if len_s1 > len_s2:
            return False
        
        s1_cnt=Counter(s1)
        window_cnt=Counter(s2[:len_s1])
        
        if s1_cnt==window_cnt:
            return True
        
        for i in range(len_s1,len_s2):
            window_cnt[s2[i]]+=1
            left_char=s2[i-len_s1]
            window_cnt[left_char]-=1
            
            if window_cnt[left_char]==0:
                del window_cnt[left_char]
            if window_cnt==s1_cnt:
                return True
        return False