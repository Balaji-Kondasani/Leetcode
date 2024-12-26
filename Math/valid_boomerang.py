#Leetcode 1037
#EASY

#APPROACH-1
#SOLUTION
class Solution(object):
    def isBoomerang(self, points):
        dy=(points[1][1]-points[0][1])
        dx=(points[1][0]-points[0][0])
        
        dy1=(points[2][1]-points[1][1])
        dx1=(points[2][0]-points[1][0])
        return dy*dx1!=dy1*dx
        
#Time Complexity -- O(1)
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted

#APPROACH-2 
#SOLUTION
class Solution(object):
    def isBoomerang(self, points):
        x1,y1=points[0]
        x2,y2=points[1] 
        x3,y3=points[2]
        area_of_triangle=abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
        if area_of_triangle!=0:
            return True
        else:
            return False         
#Time Complexity -- O(1) 
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted



