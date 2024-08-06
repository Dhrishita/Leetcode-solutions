from collections import Counter
class Solution(object):
    def minimumPushes(self, word):
        freq=Counter(word)
        sort_letters=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        
        presses=0
        letter_per_key=8
        
        for i,(letter,freq) in enumerate(sort_letters):
            curr_press=i//letter_per_key+1
            presses+=freq*curr_press
        return presses
        
        