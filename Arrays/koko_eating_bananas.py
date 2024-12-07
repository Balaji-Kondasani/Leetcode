#Leetcode 875
#MEDIUM


#BRUTE FORCE APPROACH
#SOLUTION
def canKokoPlace(self,piles,div,h):
        originalHours=0
        for i in piles:
            originalHours+=i//div
            if i%div!=0:
                originalHours+=1
        return originalHours<=h 
def minEatingSpeed(self, piles, h):
    min_eating_speed=float('inf')
    for i in range(1,max(piles)+1):
        res=self.canKokoPlace(piles,i,h)
        if res:
            min_eating_speed=min(min_eating_speed,i)
return min_eating_speed
#Time Complexity -- O(n*m) ---> where n is the number of piles and m is the maximum number of bananas in a single pile.
#Space Complexity -- O(1)
#Leetcode Verdict -- Memory Limit Exceeded


#OPTIMAL APPROACH 
#SOLUTION
def canKokoPlace(self,piles,mid,h):
        originalHours=0
        for i in piles:
            originalHours+=i//mid
            if i%mid!=0:
                originalHours+=1
        return originalHours<=h
    
       
    def minEatingSpeed(self, piles, h):
        left=1
        right=max(piles)
        while left<right:
            mid=left+(right-left)//2
            res=self.canKokoPlace(piles,mid,h)
            if res:
                right=mid
            else:
                left=mid+1
        return left
#Time Complexity -- O(Nlogw)
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted
