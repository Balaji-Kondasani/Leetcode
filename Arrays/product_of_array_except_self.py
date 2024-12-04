#LEETCODE 238
#MEDIUM

#BRUTE FORCE APPROACH

#SOLUTION
def productExceptSelf(nums):
    result=[]
    for i in range(len(nums)):
        product=1
        for j in range(len(nums)):
            if i!=j:
                product*=nums[j]
        result.append(product)
    return result
#Time Complexity -- O(n^2)
#Space Complexity -- O(1)
#Leetcode Verdict -- Time Limit Exceeded


#BETTER APPROACH

#SOLUTION
def productExceptSelf(nums):
    n=len(nums)
    left_nums=[1]*n
    right_nums=[1]*n
    
    for i in range(1,n):
        left_nums[i]=nums[i-1]*left_nums[i-1]
    for i in range(n-2,-1,-1):
        right_nums[i]=nums[i+1]*right_nums[i+1]
        
    result=[0]*n
    for i in range(n):
        result[i]=left_nums[i]*right_nums[i]
    return result
#Time Complexity -- O(n)
#Space Complexity -- O(1)
#Leetcode Verdict -- Acccepted


#OPTIMAL APPROACH
     
#SOLUTION
def productExceptSelf(nums):
    n=len(nums)
    result=[1]*n
    
    for i in range(1,n):
        result[i]=nums[i-1]*result[i-1]
    right=1
    for i in range(n-1,-1,-1):
        result[i]=result[i]*right
        right=right*nums[i]
    return result
#Time Complexity -- O(n)
#Space Complexity -- O(1)
#Leetcode Verdict -- Acccepted

    
#DIVISION APPROACH

#SOLUTION
def productExceptSelf(nums):
    count=0
    product=1
    result=[]
    for i in nums:
        if i==0:
            count+=1
        else:
            product*=i
    for i in range(len(nums)):
        if nums[i]==0:
            count-=1
            if count>0:
                result.append(0)
            else:
                result.append(product)
            count+=1
        else:
            if count>0:
                result.append(0)
            else:
                result.append(product//nums[i])
    return result
#Time Complexity -- O(n)
#Space Complexity -- O(1)
#Leetcode Verdict -- Acccepted


#EXPLANATION for Division Approach (Not Recommended):
'''
This problem can also be resolved using a division approach; however, doing so is not permitted according to the
question's requirements.
“However, let’s take a  look at it.”
We can calculate the product of the entire array in O(n) time, and then iterate through the array, dividing the total product by each element to get the result. This approach eliminates each number’s contribution by dividing it out, providing the desired output.

But we have some edge cases here:

For example : let nums=[2, 0 , 0, 4] and product_array=2*0*0*0*4=0

Now when we try dividing a non-zero number by 0 , we encounter division by zero error

Now how to solve this. Well its easy .

We maintain a counter to track the number of zeroes in the array and a product variable to store the product of all non-zero numbers.

For each nums[i]:

If nums[i] is 0, we decrement the zero counter.

If there are more than one zeroes (count_of_zeroes > 0), the result for that index is 0.

Otherwise, the result is the product of all non-zero numbers.





Explanation:

EXAMPLE: nums= [2,0,0,4]  , count_zeroes=2 , product_without_zeroes=8

 (a) for nums[0]=2 --> 

      Since count_zeroes>0 therefore for 

      nums[0] in product[0] = 0

 (b) for nums[1]=0 

      count-=1 , but count_zeroes>0 ie, 1

      therefore for nums[1] in product[1]=0

  and so on..............
'''       
        
        