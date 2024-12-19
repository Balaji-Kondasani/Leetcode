#Leetcode 258
#MEDIUM


#BRUTE FORCE APPROACH
#SOLUTION
class Solution:
    def get_count_digits(self, num):
        self.sum = 0
        count = 0
        
        while num:
            self.sum += num % 10
            num //= 10
            count += 1
            
        return count
        
    def addDigits(self, num):
        while self.get_count_digits(num) > 1:
            num = self.sum
        return self.sum

        
#Time Complexity -- O(log(num))
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted


#OPTIMAL APPROACH 
#SOLUTION
class Solution(object):
    def addDigits(self, num):
        if num==0:
            return 0
        if num%9==0:
            return 9
        if num%9!=0:
            return num%9
                  
#Time Complexity -- O(1)
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted



