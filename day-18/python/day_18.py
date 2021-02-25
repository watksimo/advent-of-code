def remove_first_bracket(exp_string, eval_func):
    open_idx = exp_string.find('(')
    close_idx = 0
    open_brack_cnt = 0
    for idx, val in enumerate(exp_string):
        if idx <= open_idx: continue
        if val == '(': open_brack_cnt += 1
        if val == ")":
            if open_brack_cnt == 0:
                close_idx = idx
                break
            else:
                open_brack_cnt -= 1
    mid_string = exp_string[open_idx+1:close_idx]
    return exp_string[:open_idx] + str(eval_func(mid_string)) + exp_string[close_idx+1:]

def regular_evaluate_expression(exp_string):
    if len(exp_string.strip().split(" ")) == 1:
        return int(exp_string.strip())

    new_string = ""

    if '(' in exp_string:
        new_string = remove_first_bracket(exp_string, regular_evaluate_expression)
    elif '*' in exp_string or '/' in exp_string:
        exp_array = exp_string.split(" ")
        new_array = []
        op_idx = 0
        for idx, val in enumerate(exp_array):
            if val in ['*', '/']:
                op_idx = idx
                break
        if op_idx > 2:
            new_array = exp_array[:op_idx-1]

        new_array.append(perform_operation(exp_array[op_idx-1], exp_array[op_idx+1], exp_array[op_idx]))
        new_array.extend(exp_array[op_idx+2:])
        new_string = " ".join(new_array)
    elif '+' in exp_string or '-' in exp_string:
        exp_array = exp_string.split(" ")
        new_array = []
        op_idx = 0
        for idx, val in enumerate(exp_array):
            if val in ['+', '-']:
                op_idx = idx
                break
        if op_idx > 2:
            new_array = exp_array[:op_idx-1]

        new_array.append(perform_operation(exp_array[op_idx-1], exp_array[op_idx+1], exp_array[op_idx]))
        new_array.extend(exp_array[op_idx+2:])
        new_string = " ".join(new_array)
    
    else:
        print("Unhandled")
        exit(1)
        
    return regular_evaluate_expression(new_string)

def part1_evaluate_expression(exp_string):
    if len(exp_string.strip().split(" ")) == 1:
        return int(exp_string.strip())

    new_string = ""

    if '(' in exp_string:
        new_string = remove_first_bracket(exp_string, part1_evaluate_expression)
    elif '*' in exp_string or '/' in exp_string or '+' in exp_string or '-' in exp_string:
        exp_array = exp_string.split(" ")
        new_array = []
        op_idx = 0
        for idx, val in enumerate(exp_array):
            if val in ['*', '/', '+', '-']:
                op_idx = idx
                break
        if op_idx > 2:
            new_array = exp_array[:op_idx-1]

        new_array.append(perform_operation(exp_array[op_idx-1], exp_array[op_idx+1], exp_array[op_idx]))
        new_array.extend(exp_array[op_idx+2:])
        new_string = " ".join(new_array)
    
    else:
        print("Unhandled")
        exit(1)
    
    
    return part1_evaluate_expression(new_string)

def part2_evaluate_expression(exp_string):
    if len(exp_string.strip().split(" ")) == 1:
        return int(exp_string.strip())

    new_string = ""

    if '(' in exp_string:
        new_string = remove_first_bracket(exp_string, part2_evaluate_expression)
    elif '+' in exp_string or '-' in exp_string:
        exp_array = exp_string.split(" ")
        new_array = []
        op_idx = 0
        for idx, val in enumerate(exp_array):
            if val in ['+', '-']:
                op_idx = idx
                break
        if op_idx > 2:
            new_array = exp_array[:op_idx-1]

        new_array.append(perform_operation(exp_array[op_idx-1], exp_array[op_idx+1], exp_array[op_idx]))
        new_array.extend(exp_array[op_idx+2:])
        new_string = " ".join(new_array)
    elif '*' in exp_string or '/' in exp_string:
        exp_array = exp_string.split(" ")
        new_array = []
        op_idx = 0
        for idx, val in enumerate(exp_array):
            if val in ['*', '/']:
                op_idx = idx
                break
        if op_idx > 2:
            new_array = exp_array[:op_idx-1]

        new_array.append(perform_operation(exp_array[op_idx-1], exp_array[op_idx+1], exp_array[op_idx]))
        new_array.extend(exp_array[op_idx+2:])
        new_string = " ".join(new_array)
    
    else:
        print("Unhandled")
        exit(1)
        
    return part2_evaluate_expression(new_string)

def perform_operation(val1, val2, operator):
    if operator == "*":
        return str(int(val1) * int(val2))
    if operator == "/":
        return str(int(val1) / int(val2))
    if operator == "+":
        return str(int(val1) + int(val2))
    if operator == "-":
        return str(int(val1) - int(val2))

if __name__=="__main__":
    input_filename = "real_input.txt"
    f = open(input_filename, "r")
    line_array = [line.strip() for line in f.readlines()]

    result1_sum = sum([part1_evaluate_expression(line_exp) for line_exp in line_array])
    print("Part 1: Sum of all values is: {}".format(result1_sum))

    result2_sum = sum([part2_evaluate_expression(line_exp) for line_exp in line_array])
    print("Part 2: Sum of all values is: {}".format(result2_sum))