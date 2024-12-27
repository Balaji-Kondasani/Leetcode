#Leetcode 342
#EASY

#APPROACH-1
#SOLUTION
class Solution(object):
    def isPowerOfFour(self, n):
        if n==0:
            return False
        while(n%4==0):
            n/=4
        if n==1:
            return True
        return False
        
#Time Complexity -- O(log base 4 (n))
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted

#APPROACH-2 
#SOLUTION
class Solution(object):
    def isPowerOfFour(self, n):
        if n<=0:
            return False
        x=math.log(n)/math.log(4)
        x=int(x)
        if math.pow(4,x)==n:
            return True
        return False             
#Time Complexity -- O(log(n)+log(x)) 
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted

#APPROACH-3
#SOLUTION
class Solution(object):
    def isPowerOfFour(self, n):
        if n<=0:
            return False
        if n&n-1==0 and (n-1)%3==0:
            return True
        return False        
#Time Complexity -- O(1) 
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted


