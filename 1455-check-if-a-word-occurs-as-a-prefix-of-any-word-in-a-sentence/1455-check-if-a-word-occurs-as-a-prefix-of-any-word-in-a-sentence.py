class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        words=sentence.split()  
        for index,word in enumerate(words,start=1):  
            if word.startswith(searchWord):  
                return index
        return -1 
        