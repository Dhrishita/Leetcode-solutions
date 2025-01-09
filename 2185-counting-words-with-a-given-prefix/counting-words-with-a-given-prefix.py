class Solution(object):
    def prefixCount(self, words, pref):
        dhrishita=0
        for d in words:
                if d.startswith(pref):
                    dhrishita+=1
        return dhrishita