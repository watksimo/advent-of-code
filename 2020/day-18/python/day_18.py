def evaluate_first_bracket(exp_string):
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
    bracket_string = exp_string[open_idx+1:close_idx]
    start_string = exp_string[:open_idx]
    end_string = exp_string[close_idx+1:]
    return bracket_string, start_string, end_string

def operators_in_string(exp_string, op_array):
    for oper in op_array:
        if oper in exp_string: return True
    return False

def evaluate_expression(exp_string, oper_prec_array):
    # Recursion base case
    if len(exp_string.strip().split(" ")) == 1:
        return int(exp_string.strip())

    new_string = ""

    if '(' in exp_string:
        bracket_string, start_string, end_string = evaluate_first_bracket(exp_string)
        bracket_string = evaluate_expression(bracket_string, oper_prec_array)
        new_string = start_string + str(bracket_string) + end_string
    else:
        for op_prec in oper_prec_array:
            if operators_in_string(exp_string, op_prec):
                exp_array = exp_string.split(" ")
                new_array = []
                op_idx = 0
                for idx, val in enumerate(exp_array):
                    if val in op_prec:
                        op_idx = idx
                        break
                if op_idx > 2:
                    new_array = exp_array[:op_idx-1]

                new_array.append(perform_operation(exp_array[op_idx-1], exp_array[op_idx+1], exp_array[op_idx]))
                new_array.extend(exp_array[op_idx+2:])
                new_string = " ".join(new_array)
                break
        
    return evaluate_expression(new_string, oper_prec_array)

def perform_operation(val1, val2, operator):
    operation_switcher = {
        "*": str(int(val1) * int(val2)),
        "/": str(int(val1) / int(val2)),
        "+": str(int(val1) + int(val2)),
        "-": str(int(val1) - int(val2))
    }
    try:
        return operation_switcher[operator]
    except KeyError:
        print(f"{operator} is not a handled operator.")
        exit(1)

if __name__=="__main__":
    input_filename = "real_input.txt"
    f = open(input_filename, "r")
    line_array = [line.strip() for line in f.readlines()]

    part1_oper_prec = [['*', '/', '+', '-']]
    part2_oper_prec = [['+', '-'], ['*', '/']]

    part1_results = []
    part2_results = []

    for line_exp in line_array:
        part1_results.append(evaluate_expression(line_exp, part1_oper_prec))
        part2_results.append(evaluate_expression(line_exp, part2_oper_prec))

    print(f"Part 1: Sum of all values is: {sum(part1_results)}")
    print(f"Part 2: Sum of all values is: {sum(part2_results)}")