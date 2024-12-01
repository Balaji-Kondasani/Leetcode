#LEETCODE 121
#EASY

#BRUTE FORCE APPROACH
#Solution
def Stock_Price_calculator(prices):
    profit=float('-inf')
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[j]>prices[i]:
                max_profit=prices[j]-prices[i]
                profit=max(profit,max_profit)
    return profit
#Time Complexity -- O(n^2)
#Space Complexity -- O(1)
#Leetcode Verdict -- Time Limit Exceeded


#OPTIMAL APPROACH
#Solution
def Stock_Price_calculator(prices):
    buy_price=prices[0]
    profit=0
    for i in range(1,len(prices)):
        if prices[i]<buy_price:
            buy_price=prices[i]
        else:
            current_profit=prices[i]-buy_price
            profit=max(current_profit,profit)
    return profit
#Time Complexity -- O(n)
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted