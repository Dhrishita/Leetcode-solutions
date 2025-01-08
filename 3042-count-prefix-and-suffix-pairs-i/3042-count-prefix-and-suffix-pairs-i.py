class Solution(object):
    def countPrefixSuffixPairs(self, words):
        def isPrefixAndSuffix(str1, str2):
            return str2.startswith(str1) and str2.endswith(str1)
        dhrishita=0
        for d in range(len(words)):
            for m in range(d+1,len(words)):
                if isPrefixAndSuffix(words[d],words[m]):
                    dhrishita+=1
        return dhrishita