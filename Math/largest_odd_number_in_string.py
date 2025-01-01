#Leetcode 1903
#EASY

#APPROACH-1
#SOLUTION    
    def largestOddNumber(self, num):
        n = len(num)
        for i in range(n - 1, -1, -1):
            if (int(num[i]) % 2 != 0):
                return num[:i + 1]
        
        return ""
#Time Complexity -- O(n) 
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted

