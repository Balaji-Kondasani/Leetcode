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
            return [hashmap[target-nums[i]],i]
        else:
            hashmap[nums[i]]=i
list1=[2,7,11,15]
target=9
result=pairSum(list1,target)
print(result)
#Time Complexity -- O(n)
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted
