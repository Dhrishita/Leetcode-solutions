from collections import Counter
class Solution(object):
    def wordSubsets(self, words1, words2):
        max_freq=Counter()
        for word in words2:
            word_count=Counter(word)
            for char in word_count:
                max_freq[char]=max(max_freq[char], word_count[char])
        dhrishita=[]
        for word in words1:
            word_count=Counter(word)
            if all(word_count[char]>=max_freq[char] for char in max_freq):
                dhrishita.append(word)
        return dhrishita