#Leetcode 319
#MEDIUM


#BRUTE FORCE APPROACH
#SOLUTION
class Solution(object):
    def bulbSwitch(self, n):
        count=0
        for i in range(1,n+1):
            squa_number=int(math.sqrt(i))
            if (squa_number*squa_number)==i:
                count+=1
        return count
        
#Time Complexity -- O(n)
#Space Complexity -- O(1)
#Leetcode Verdict -- Time Limit Exceeded


#OPTIMAL APPROACH 
#SOLUTION
class Solution(object):
    def bulbSwitch(self, n):
        return int(math.sqrt(n))
                  
#Time Complexity -- O(1)
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted


