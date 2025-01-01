#Leetcode 867
#EASY

#APPROACH-1
#SOLUTION    
    def transpose(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        result = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                result[j][i]=matrix[i][j]
        return result
#Time Complexity -- O(m*n) 
#Space Complexity -- O(1) We ignore the space taken for result
#Leetcode Verdict -- Accepted


