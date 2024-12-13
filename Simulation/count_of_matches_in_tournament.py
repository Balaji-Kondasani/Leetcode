#Leetcode 1688
#EASY

#BRUTE FORCE APPROACH
#SOLUTION
class Solution(object):
    def numberOfMatches(self, n):
        matches=0
        while n>1:
            if n%2==0:
                matches+=n/2
                n=n/2
            else:
                matches+=(n-1)/2
                n=(n-1)/2+1
        return matches
#Time Complexity -- O(logn) 
#Space Complexity -- O(1) 
#Leetcode Verdict -- Accepted


#OPTIMAL APPROACH
#SOLUTION
class Solution(object):
    def numberOfMatches(self, n):
        return n-1
#Time Complexity -- O(1)
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted

 