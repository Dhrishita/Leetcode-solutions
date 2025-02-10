class Solution(object):
    def clearDigits(self, s):
        d_stack=[]
        for char in s:
            if char.isdigit():
                if d_stack:
                    d_stack.pop()
            else:
                d_stack.append(char)
        return "".join(d_stack)