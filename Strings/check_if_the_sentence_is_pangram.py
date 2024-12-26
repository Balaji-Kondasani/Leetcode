#Leetcode 1832
#HARD

#APPROACH-1
#SOLUTION
class Solution(object):
    def checkIfPangram(self, sentence):
        arr=[0]*26
        ch=ord("a")
        count=0
        for i in sentence:
            index=ord(i)-ch
            if arr[index]==0:
                count+=1
                arr[index]+=1
            else:
                arr[index]+=1
        if count==26:
            return True
        else:
            return False
#Time Complexity -- O(n) 
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted

#APPROACH-2
#SOLUTION
class Solution(object):
    def checkIfPangram(self, sentence):
        return len(set(sentence))==26
#Time Complexity -- O(n) 
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted


        



