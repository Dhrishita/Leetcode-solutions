class Solution:
    def diffWaysToCompute(self,expression):
        if expression.isdigit():
            return [int(expression)]
        d_ans=[]
        
        for i, char in enumerate(expression):
            if char in "+-*":
                left_results=self.diffWaysToCompute(expression[:i])
                right_results=self.diffWaysToCompute(expression[i+1:])
                
                for left in left_results:
                    for right in right_results:
                        if char=='+':
                            d_ans.append(left+right)
                        elif char=='-':
                            d_ans.append(left-right)
                        elif char=='*':
                            d_ans.append(left*right)
        return d_ans
