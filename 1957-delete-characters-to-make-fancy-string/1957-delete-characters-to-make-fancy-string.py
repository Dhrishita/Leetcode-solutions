class Solution(object):
    def makeFancyString(self, s):
        ans=[]
    
        for char in s:
            if len(ans)>=2 and ans[-1] == char and ans[-2] == char:
                continue
            ans.append(char)
        return ''.join(ans)