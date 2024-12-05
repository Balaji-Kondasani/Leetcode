#Leetcode 34
#MEDIUM


#BRUTE FORCE APPROACH
#SOLUTION
def searchRange(self, nums, target):
    first_occurence=-1
    last_occurence=-1
    for i in range(len(nums)):
        if nums[i]==target:
            if first_occurence==-1:
                first_occurence=i
            last_occurence=i
    return [first_occurence,last_occurence]
#Time Complexity -- O(n)
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted


#OPTIMAL APPROACH (BINARY SEARCH)
#SOLUTION
def findLeftMost(self, nums, target):
        l, r = 0, len(nums) - 1
        first_found = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                first_found = mid
                r = mid - 1  
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return first_found

def findRightMost(self, nums, target):
    l, r = 0, len(nums) - 1
    last_found = -1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            last_found = mid
            l = mid + 1  
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return last_found

def searchRange(self, nums, target):
    first_found = self.findLeftMost(nums, target)
    last_found = self.findRightMost(nums, target)
    return [first_found, last_found]

#Time Complexity -- O(logn)
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted