#LEETCODE 35
#EASY

#BRUTE FORCE APPROACH


#SOLUTION
def searchInsert(self, nums, target):
    for i in range(len(nums)):
        if nums[i]<target and i==len(nums)-1:
            return i+1
        elif nums[i]<target and i<len(nums)-1:
            continue
        elif nums[i]==target:
            return i
        else:
            if nums[i]>target:
            return i
#Time Complexity -- O(n)
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted
        

#OPTIMAL APPROACH

#SOLUTION
def searchInsert(nums,target):
    beg=0
    end=len(nums)-1
    while beg<=end:
        mid=(beg+end)//2
        if nums[mid]==target:
            found=True
            return mid
        elif nums[mid]>target:
            end=mid-1
        else:
            beg=mid+1
    return beg
#Time Complexity -- O(logn)
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted
