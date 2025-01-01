#Leetcode 48
#MEDIUM


#BRUTE FORCE APPROACH
#SOLUTION
def rotate(self,matrix):
    if not matrix or not matrix[0]:
        return
    
    n = len(matrix)      
    m = len(matrix[0])    
    
    rotated = [[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            rotated[j][n - 1 - i] = matrix[i][j]
    
    for i in range(m):
        for j in range(n):
            matrix[i][j] = rotated[i][j]


#Time Complexity -- O(m*n) where m is no of rows and n is columns
#Space Complexity -- O(m*n)
#Leetcode Verdict -- Accepted


#OPTIMAL APPROACH 
#SOLUTION
class Solution:
    def rotate(self, matrix):
        N = len(matrix)

        
        for i in range(N):
            for j in range(i, N):
             
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(N):
            matrix[i].reverse()

#Time Complexity -- O(n^2)
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted
