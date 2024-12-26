#Leetcode 859
#EASY

#SOLUTION
class Solution(object):
    def checkFreq(self, s):
        arr = [0] * 26
        
        for ch in s:
            arr[ord(ch) - ord('a')] += 1
            
            if arr[ord(ch) - ord('a')] > 1:
                return True
        
        return False
    
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False
        
        if s == goal:
           
            return self.checkFreq(s)
        
        indices = []
        
        for i in range(len(s)):
            if s[i] != goal[i]:
                indices.append(i)
        
        if len(indices) != 2:
            return False
        
        first, second = indices
        
        s_list = list(s) 
        s_list[first], s_list[second] = s_list[second], s_list[first]
        
        return ''.join(s_list) == goal

        #Time Complexity -- O(n) 
        #Space Complexity -- O(n)
