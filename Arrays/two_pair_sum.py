#Leetcode 1
#EASY

#BRUTE FORCE APPROACH

#SOLUTION
def pairSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
#Time Complexity -- O(n^2)
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted
            
#OPTIMAL SOLUTION
            
#SOLUTION
def pairSum(nums,target):
    hashmap={}
    for i in range(len(nums)):
        if target-nums[i] in hashmap:
            return [i,hashmap[target-nums[i]]]
        else:
            hashmap[nums[i]]=i
#Time Complexity -- O(n)
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted
