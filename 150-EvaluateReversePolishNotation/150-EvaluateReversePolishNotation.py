# Last updated: 07/04/2026, 11:40:50
import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize an empty stack to keep track of operands
        stack = []
        
        # Define the set of operators
        operators = {'+', '-', '*', '/'}
        
        # If there's only one token, return its integer value
        if len(tokens) == 1: 
            return int(tokens[0])
        
        # Iterate through each token in the input list
        for token in tokens:
            # If the token is not an operator, push it as an integer onto the stack
            if token not in operators:
                stack.append(int(token))
            else:
                # If it's an operator, pop the top two operands from the stack
                sec_operand = stack.pop()
                fir_operand = stack.pop()
                tmp = 0
                
                # Perform the corresponding operation based on the operator
                if token == '+':
                    tmp = fir_operand + sec_operand
                elif token == '-':
                    tmp = fir_operand - sec_operand
                elif token == '*':
                    tmp = fir_operand * sec_operand
                elif token == '/':
                    # Perform integer division and truncate the result
                    tmp = fir_operand / sec_operand
                    tmp = math.trunc(tmp)
                
                # Push the result back onto the stack
                stack.append(tmp)
        
        # The final result is the only element left on the stack
        return stack.pop()