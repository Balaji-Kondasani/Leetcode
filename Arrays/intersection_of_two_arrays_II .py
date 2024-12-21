#Leetcode 350
#EASY


#BRUTE FORCE APPROACH
#SOLUTION
class Solution(object):
    def intersect(self, nums1, nums2):
        result=[]
        hashmap={}
        for i in nums1:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        for j in nums2:
            if j in hashmap and hashmap[j]>0:
                hashmap[j]-=1
                result.append(j)
        return result
#Time Complexity -- O(n) 
#Space Complexity -- O(n)
#Leetcode Verdict -- Accepted


#OPTIMAL APPROACH 
#SOLUTION
class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        i,j=0,0
        result=[]
        while i<len(nums1) and j < len(nums2):
            if nums1[i]==nums2[j]:
                result.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                i+=1
        return result          
#Time Complexity -- O(n)+O(nlogn)
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted

