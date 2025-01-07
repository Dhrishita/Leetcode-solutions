class Solution(object):
    def stringMatching(self, words):
        dhrishita=[]
        words.sort(key=len)
        for d in range(len(words)):
            for m in range(d+1,len(words)):
                if words[d] in words[m]:
                    dhrishita.append(words[d])
                    break
        return dhrishita

        
        
