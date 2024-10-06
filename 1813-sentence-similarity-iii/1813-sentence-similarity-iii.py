class Solution(object):
    def areSentencesSimilar(self, sentence1, sentence2):
        s1=sentence1.split()
        s2=sentence2.split()
        
        if len(s1)<len(s2):
            s1,s2=s2,s1
        
        d=0
        while d<len(s2) and s1[d]==s2[d]:
            d+=1
        
        m=0
        while m<len(s2)-d and s1[-(m+1)]==s2[-(m+1)]:
            m+=1
        return d+m==len(s2)