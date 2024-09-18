from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        # Convert all integers to strings for comparison
        num_str = list(map(str, nums))
        
        # Define a custom comparator function
        def compare(x, y):
            # Compare two numbers based on their concatenated values
            if x + y > y + x:
                return -1  # x should come before y
            elif x + y < y + x:
                return 1  # y should come before x
            else:
                return 0  # they are equal
        
        # Sort numbers using the custom comparator
        num_str.sort(key=cmp_to_key(compare))
        
        # Join the sorted numbers to form the largest number
        largest = ''.join(num_str)
        
        # Edge case: if the largest number is '0', return '0' instead of '000...'
        return '0' if largest[0] == '0' else largest
