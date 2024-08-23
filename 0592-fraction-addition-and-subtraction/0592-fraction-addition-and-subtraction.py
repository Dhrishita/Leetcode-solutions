import math
class Solution(object):
    def gcd(self,d,m):
        while m:
            d,m =m,d%m
        return d
    
    def fractionAddition(self,expression):
        i,n=0,len(expression)
        num,deno=0,1
        
        while i<n:
            sign=1
            if expression[i]=='-':
                sign=-1
                i+=1
            elif expression[i]=='+':
                i+=1
            
            curr_num=0
            while i<n and expression[i].isdigit():
                curr_num=curr_num*10+int(expression[i])
                i+=1
            curr_num*=sign
            i+=1
            
            curr_deno=0
            while i<n and expression[i].isdigit():
                curr_deno=curr_deno*10+int(expression[i])
                i+=1
            
            lcm=deno*curr_deno//self.gcd(deno,curr_deno)
            num=num*(lcm//deno)+curr_num*(lcm//curr_deno)
            deno=lcm
        
        common_gcd=self.gcd(abs(num),deno)
        num//=common_gcd
        deno//=common_gcd
        return "{}/{}".format(num,deno)