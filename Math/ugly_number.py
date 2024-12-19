#Leetcode 258
#MEDIUM


#APPROACH-1
#SOLUTION
class Solution(object):
    def isUgly(self, n):
        while n>1:
            if n==0:
                return False
            if n==1:
                return False
            if n%2==0:
                n=n/2
            elif n%3==0:
                n=n/3
            elif n%5==0:
                n=n/5
            else:
                return False
        if n==1:
            return True
        else:
            return False
#Time Complexity -- O(k) where k is no of iteration required for digits
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted



