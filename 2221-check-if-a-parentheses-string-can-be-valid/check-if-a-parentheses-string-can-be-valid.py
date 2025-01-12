class Solution(object):
    def canBeValid(self, s, locked):
        n = len(s)
        if n % 2 != 0:
            return False
        
        min_open, max_open = 0, 0
        
        for i in range(n):
            if locked[i] == '1':
                if s[i] == '(':
                    min_open += 1
                    max_open += 1
                else:
                    min_open -= 1
                    max_open -= 1
            else:
                max_open += 1
                min_open -= 1
            
            min_open = max(min_open, 0)
            if max_open < 0:
                return False
        
        min_open, max_open = 0, 0
        
        for i in range(n - 1, -1, -1):
            if locked[i] == '1':
                if s[i] == ')':
                    min_open += 1
                    max_open += 1
                else:
                    min_open -= 1
                    max_open -= 1
            else:
                max_open += 1
                min_open -= 1
            
            min_open = max(min_open, 0)
            if max_open < 0:
                return False
        return min_open == 0
