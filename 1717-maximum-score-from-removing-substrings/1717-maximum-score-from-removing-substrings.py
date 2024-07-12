class Solution(object):
    def maximumGain(self, s, x, y):
        def remove_substring(s,sub,points):
            stack=[]
            score=0
            for char in s:
                if stack and stack[-1]+char==sub:
                    stack.pop()
                    score+=points
                else:
                    stack.append(char)
            return "".join(stack),score
        
        if x>=y:
            s,score1=remove_substring(s,"ab",x)
            s,score2=remove_substring(s,"ba",y)
        else:
             s,score1=remove_substring(s,"ba",y)
             s,score2=remove_substring(s,"ab",x)
        return score1+score2
                    
       
        