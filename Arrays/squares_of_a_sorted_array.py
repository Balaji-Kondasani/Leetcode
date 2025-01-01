#Leetcode 977
#EASY

#APPROACH-1 (Brute Force)
#SOLUTION    
    def sortedSquares(self, nums):
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        nums.sort()
        return nums


#Time Complexity -- O(nlog(n)) 
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted

#APPROACH-2 (Optimal)
#SOLUTION
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        
        i = 0
        j = n - 1
        k = n - 1
        
        while k >= 0:
            a = nums[i] * nums[i]
            b = nums[j] * nums[j]
            
            if a > b:
                result[k] = a
                i += 1
            else:
                result[k] = b
                j -= 1
            k -= 1
            
        return result

#Time Complexity -- O(n) 
#Space Complexity -- O(1) Extra space taken for storing result would not be conidered.
#Leetcode Verdict -- Accepted
