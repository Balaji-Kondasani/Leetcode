#Leetcode 976
#EASY

#APPROACH-1
#SOLUTION
class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort()
        n=len(nums)
        for i in range(n-3,-1,-1):
            if nums[i]+nums[i+1]>nums[i+2]:
                return nums[i]+nums[i+1]+nums[i+2]
        return 0
#Time Complexity -- O(nlogn+n) 
#Space Complexity -- O(1)