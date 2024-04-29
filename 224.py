class Solution:
    def calculate(self, s: str) -> int:
        priors = {
            "+":1,
            "-":1,
            "*":2,
            "/":2,
            "-unary": 3
        }
        op_stack = []
        args_stack = []

        def get_num_and_new_i(s, i):
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            num = int(s[start:i])
            return i-1, num

        def calc_prev_op():
            op = op_stack.pop()
            if op == "-unary":
                res = -args_stack.pop()
            else:
                arg2 = args_stack.pop()
                arg1 = args_stack.pop()

                if op == "+":
                    res = arg1 + arg2
                elif op == "-":
                    res = arg1 - arg2
                elif op == "*":
                    res = arg1 * arg2
                elif op == "/":
                    res = int(arg1 / arg2)
            
            args_stack.append(res)
        
        prev_start_op = True
        i = 0
        while i < len(s):
            c = s[i]
            if prev_start_op and c == "-":
                c = "-unary"
            if c in priors:
                while len(op_stack)>0 and op_stack[-1] != "(" and priors[op_stack[-1]] >= priors[c]:
                    calc_prev_op()
                op_stack.append(c)
                prev_start_op = True
            elif c == "(":
                op_stack.append(c)
                prev_start_op = True
            elif c == ")":
                while op_stack[-1] != "(":
                    calc_prev_op()
                op_stack.pop()
                prev_start_op = False
            elif c.isdigit():
                i, num = get_num_and_new_i(s, i)
                args_stack.append(num)
                prev_start_op = False
            i += 1

        while len(op_stack) > 0:
            calc_prev_op()
        
        return args_stack[0]
