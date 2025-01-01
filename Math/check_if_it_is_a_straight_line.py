#Leetcode 1232
#EASY

#APPROACH-1
#SOLUTION
def checkStraightLine(self, coordinates):
        if len(coordinates)<2:
            return False
        dy=coordinates[1][1]-coordinates[0][1]
        dx=coordinates[1][0]-coordinates[0][0]

        for i in range(2,len(coordinates)):
            dy1=coordinates[i][1]-coordinates[0][1]   
            dx1=coordinates[i][0]-coordinates[0][0]

            if dy*dx1==dx*dy1:
                continue
            else:
                return False
        return True

#Time Complexity -- O(n) 
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted
