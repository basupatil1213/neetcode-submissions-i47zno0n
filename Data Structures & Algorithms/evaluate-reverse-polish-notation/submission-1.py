class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val_stack = []

        def get_result(first_val, second_val, operation):
            if operation == '+':
                return first_val + second_val
            elif operation == '-':
                return first_val - second_val
            elif operation == '*':
                return first_val * second_val
            return int(first_val / second_val)

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                second_val = val_stack.pop()
                first_val = val_stack.pop()
                result = get_result(first_val, second_val, token)
                val_stack.append(result)    
            else:
                val_stack.append(int(token))

        return val_stack[0]
        