#Leetcode 70
#EASY

#BRUTE FORCE APPROACH (Recursion)
#SOLUTION
class Solution(object):
    def solve(self,n):
        if n<0:
            return 0
        if n==0:
            return 1
        first=self.solve(n-1)
        second=self.solve(n-2)
        return  first+second     
    def climbStairs(self, n):
        return self.solve(n)
#Time Complexity -- O(2^n) 
#Space Complexity -- O(n) --- > Due to Recursive Call Stack
#Leetcode Verdict -- Time Limit Exceeded


#BETTER APPROACH (Memoization)
#SOLUTION
class Solution(object):
    memo={1:1,2:2}
    def solve(self,n):
        if n in self.memo:
            return self.memo[n]
        else:
            self.memo[n]=self.solve(n-1)+self.solve(n-2)
            return self.memo[n]   
    def climbStairs(self, n):
        return self.solve(n)              
#Time Complexity -- O(n)
#Space Complexity -- O(n)
#Leetcode Verdict -- Accepted

#OPTIMAL APPROACH (Dynamic Programming)
#SOLUTION
class Solution(object):
    def climbStairs(self, n):
        if n==0 or n==1 or n==2:
            return n
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
#Time Complexity -- O(n)
#Space Complexity -- O(n)
#Leetcode Verdict -- Accepted

        
