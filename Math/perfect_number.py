#Leetcode 507
#EASY

#BRUTE FORCE APPROACH
#SOLUTION
class Solution(object):
    def checkPerfectNumber(self, num):
        result=0
        for i in range(1,num-1):
            if num%i==0:
                result+=i
        if result==num:
            return True
        else:
            return False
#Time Complexity -- O(n)
#Space Complexity -- O(1)
#Leetcode Verdict -- Time Limit Exceeded

#OPTIMAL APPROACH 
#SOLUTION
class Solution(object):
    def checkPerfectNumber(self, num):
        result=0
        for i in range(1,num-1):
            if num%i==0:
                result+=i
            if result>num:
                return False
        return result==num
#Time Complexity -- O(n) 
#Space Complexity -- O(1)
#Leetcode Verdict -- Time Limit Exceeded


#OPTIMAL APPROACH 
#SOLUTION
class Solution(object):
    def checkPerfectNumber(self, num):
        if num==1:
            return False
        result=1
        sqrt_num=int(sqrt(num))
        for i in range(2,sqrt_num+1):
            if num%i==0:
                result+=(i+num/i)
            if result>num:
                return False
        return result==num               
#Time Complexity -- O(sqrt(n)) 
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted


