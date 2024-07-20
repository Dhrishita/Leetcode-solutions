class Solution(object):
    def luckyNumbers (self, matrix):
        min_in_row=[min(row) for row in matrix]
        lucky_numbers=[]
        
        for i in range (len(matrix)):
            for j in range (len(matrix[0])):
                if matrix[i][j]==min_in_row[i]:
                    if all(matrix[k][j]<=matrix[i][j] for k in range (len(matrix))):
                        lucky_numbers.append(matrix[i][j])
        return lucky_numbers
        