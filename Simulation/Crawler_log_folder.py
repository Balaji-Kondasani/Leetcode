#Leetcode 1598
#EASY

#BRUTE FORCE APPROACH
#SOLUTION
class Solution(object):
    def minOperations(self, logs):
        stack=[]
        for i in logs:
            if i =="../":
                if stack:
                    stack.pop()
            elif i !="./":
                stack.append(i)
        return len(stack)
#Time Complexity -- O(n) 
#Space Complexity -- O(n) 
#Leetcode Verdict -- Accepted


#OPTIMAL APPROACH
#SOLUTION
class Solution(object):
    def minOperations(self, logs):
        depth=0
        for i in logs:
            if i =="../":
                depth=max(0,depth-1)
            elif i =="./":
                continue
            else:
                depth+=1
        return depth
#Time Complexity -- O(n)
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted

 
