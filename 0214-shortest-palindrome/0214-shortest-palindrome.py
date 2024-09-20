class Solution(object):
    def shortestPalindrome(self, s):
        rev_s=s[::-1]  
        l=s+"#"+rev_s  
        d=len(l)
        kmp=[0]*d
        
        for i in range(1,d):
            m=kmp[i-1]
            while m>0 and l[i]!=l[m]:
                m=kmp[m-1]
            if l[i]==l[m]:
                m+=1
            kmp[i]=m
    
        longest_palindrome_prefix_len=kmp[-1]
        suffix_to_add=rev_s[:len(s)-longest_palindrome_prefix_len]
        return suffix_to_add+s