#Leetcode 334
#MEDIUM


#BRUTE FORCE APPROACH
#SOLUTION
def increasingTriplet(self, nums):
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]<nums[j]<nums[k]:
                    return True
    return False
#Time Complexity -- O(n^3)
#Space Complexity -- O(1)
#Leetcode Verdict -- Time Limit Exceeded


#OPTIMAL APPROACH 
#SOLUTION
def increasingTriplet(self, nums):
        n=len(nums)
        num1=float('inf')
        num2=float('inf')
        for i in range(n):
            num3=nums[i]
            if num3<=num1:
                num1=num3
            elif num3<=num2:
                num2=num3
            else:
                return True
        return False
#Time Complexity -- O(n)
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted