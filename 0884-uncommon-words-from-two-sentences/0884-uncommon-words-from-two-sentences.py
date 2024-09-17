class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        words=s1.split()+s2.split()
        count=Counter(words)
        return[word for word,freq in count.items() if freq==1]