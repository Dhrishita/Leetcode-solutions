class Solution(object):
    def reverseParentheses(self, s):
        stack=[]
        for char in s:
            if char==')':
                d=[]
                while stack and stack[-1]!='(':
                    d.append(stack.pop())
                stack.pop()
                stack.extend(d)
            else:
                stack.append(char)
        return ''.join(stack)
        