#Leetcode 50
#MEDIUM

#APPROACH-1
#SOLUTION    
    def solve(self,x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.solve(x, -n)
        if n % 2 == 0:
            return self.solve(x * x, n // 2)
        return x * self.solve(x * x, (n - 1) // 2)

    def myPow(self,x, n):
        return self.solve(x, n)

#Time Complexity -- O(log(n)) 
#Space Complexity -- O(log(n))
#Leetcode Verdict -- Accepted

#APPROACH-2
#SOLUTION
    def myPow(self,x, n):
        return x**n

#Time Complexity -- O(log(n)) 
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted