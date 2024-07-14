import collections
import re
class Solution(object):
    def countOfAtoms(self, formula):
        pattern=r'([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)'
        tokens=re.findall(pattern, formula)
        stack=[collections.defaultdict(int)]
        
        i = 0
        while i<len(tokens):
            if tokens[i][0]: 
                element=tokens[i][0]
                count=int(tokens[i][1]) if tokens[i][1] else 1
                stack[-1][element]+=count
            elif tokens[i][2]:  
                stack.append(collections.defaultdict(int))
            elif tokens[i][3]:  
                top=stack.pop()
                multiplier=int(tokens[i][4]) if tokens[i][4] else 1
                for elem,cnt in top.items():
                    stack[-1][elem]+=cnt * multiplier
            i+=1
        result=stack.pop()
        sorted_elements=sorted(result.keys())
        output=[]
        for elem in sorted_elements:
            output.append(elem)
            if result[elem]>1:
                output.append(str(result[elem]))
        return ''.join(output)


