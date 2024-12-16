#Leetcode 20
#MEDIUM


#Approach-1
#SOLUTION
class Solution(object):
    def isValid(self, s):
        stack=[]
        for ch in s:
            if ch=="{" or ch=="[" or ch=="(":
                stack.append(ch)
                continue
            if ch=="}":
                if stack and stack[-1]=="{":
                    stack.pop()
                else:
                    return False
            elif ch=="]":
                if stack and  stack[-1]=="[":
                    stack.pop()
                else:
                    return False
            elif ch==")":
                if stack and stack[-1]=="(":
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
            
#Time Complexity -- O(n)
#Space Complexity -- O(n)
#Leetcode Verdict -- Accepted


#Approach-2
#SOLUTION
class Solution(object):
    def isValid(self, s):
        stack=[]
        for ch in s:
            if ch=="{":
                stack.append("}")
            elif ch=="[":
                stack.append("]")
            elif ch=="(":
                stack.append(")")
            elif not stack or stack[-1]!=ch:
                return False
            else:
                stack.pop()
        if len(stack)==0:
            return True
        else:
            return False
#Time Complexity -- O(n)
#Space Complexity -- O(n)
#Leetcode Verdict -- Accepted



