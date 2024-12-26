#Leetcode 1106
#HARD

#APPROACH-1
#SOLUTION
cclass Solution(object):
    def solve_op(self, op, values):
        if op == '!':
            return 'f' if values[0] == 't' else 't'
        
        if op == '&':
            return 'f' if any(ch == 'f' for ch in values) else 't'
        
        if op == '|':
            return 't' if any(ch == 't' for ch in values) else 'f'
        
        return 't' 

    def parseBoolExpr(self, expression):
        stack = []
        for char in expression:
            if char == ',':
                continue
            
            if char == ')':
                values = []
                while stack and stack[-1] != '(':
                    values.append(stack.pop())
                stack.pop()  
                op = stack.pop() 
                stack.append(self.solve_op(op, values[::-1])) 
            
            else:
                stack.append(char)
        
        return stack[-1] == 't'  
     
#Time Complexity -- O(1) 
#Space Complexity -- O(1)
#Leetcode Verdict -- Accepted




