#Leetcode 15
#MEDIUM


#BRUTE FORCE APPROACH
#SOLUTION
class Solution(object):
    def threeSum(self, nums):
        result=set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[k]+nums[j]==0:
                        result.add(tuple(sorted([nums[i],nums[j],nums[k]])))
        return [list(triplet) for triplet in result]        
#Time Complexity -- O(n^3)
#Space Complexity -- O(1)
#Leetcode Verdict -- Time Limit Exceeded


#OPTIMAL APPROACH 
#SOLUTION
class Solution:
    def threeSum(self, nums):
        result=[]
        if len(nums)<3:
            return []
        nums.sort()
        n=len(nums)
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            n1=nums[i]
            target=-n1
            self.twoSum(nums,target,i+1,n-1,result)
        return result
    def twoSum(self,nums,target,i,j,result):
        while i<j:
            if nums[i]+nums[j]>target:
                j-=1
            elif nums[i]+nums[j]<target:
                i+=1
            else:
                result.append([-target,nums[i],nums[j]])
                while i<j and nums[i]==nums[i+1]:
                    i+=1
                while i <j and nums[j]==nums[j-1]:
                    j-=1
                i+=1
                j-=1
#Time Complexity -- O(n^2)
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted


