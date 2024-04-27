# 2+3*4^(2+2)-6*8
def calc(s):
    priors = {
        "+":1,
        "-":1,
        "*":2,
        "/":2
    }
    op_stack = []
    args_stack = []

    def get_num_and_new_i(s, i):
        start = i
        while i < len(s) and s[i].isdigit():
            i += 1
        num = int(s[start:i])
        return i-1, num
    
    def get_num_and_new_i(s, i):
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            num = int(s[start:i])
            return i-1, num


    def calc_prev_op():
        op = op_stack.pop()
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
    
    i = 0
    while i < len(s):
        c = s[i]
        if c in priors:
            while len(op_stack)>0 and priors[op_stack[-1]] >= priors[c]:
                calc_prev_op()
            op_stack.append(c)
        elif c.isdigit():
            i, num = get_num_and_new_i(s, i)
            args_stack.append(num)
        i += 1

    while len(op_stack) > 0:
        calc_prev_op()
    
    return args_stack[0]




if __name__ == '__main__':
    print(calc("3+2*2"))
    print(calc(" 3/2 "))
    print(calc(" 3+5 / 2 "))
  
