#Leetcode 53
#MEDIUM


#BRUTE FORCE APPROACH
#SOLUTION
def maxSubArray(self, nums):
    max_Sum=float('-inf')
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            Current_sum=0
            for k in range(i,j+1):
                Current_sum+=nums[k]
            max_Sum=max(max_Sum,Current_sum)
    return max_Sum
        
#Time Complexity -- O(n^3) 
#Space Complexity -- O(1)
#Leetcode Verdict -- Time Limit Exceeded

#BETTER  APPROACH
#SOLUTION
def maxSubArray(self, nums):
    max_Sum=float('-inf')
    Current_sum=0
    for i in range(len(nums)):
        Current_sum=0
        for j in range(i,len(nums)):
            Current_sum+=nums[j]
            max_Sum=max(max_Sum,Current_sum)
    return max_Sum

#Time Complexity -- O(n^2) 
#Space Complexity -- O(1)
#Leetcode Verdict -- Time Limit Exceeded


#OPTIMAL APPROACH 
#SOLUTION
def maxSubArray(self, nums):
    max_Sum=float('-inf')
    Current_sum=0
    for i in range(len(nums)):
        Current_sum+=nums[i]
        max_Sum=max(max_Sum,Current_sum)
        if Current_sum<0:
            Current_sum=0
    return max_Sum
                    
#Time Complexity -- O(n) 
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted
