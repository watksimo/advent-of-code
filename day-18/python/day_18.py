# TODO find correct nested brackets
def regular_evaluate_expression(exp_string):
    
    if len(exp_string.strip().split(" ")) == 1:
        return int(exp_string.strip())

    new_string = ""

    if '(' in exp_string:
        mid_string = exp_string[exp_string.find('(')+1:exp_string.rfind(')')]
        new_string = exp_string[:exp_string.find('(')] + str(regular_evaluate_expression(mid_string)) + exp_string[exp_string.rfind(')')+1:]
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
    print(exp_string)
    if len(exp_string.strip().split(" ")) == 1:
        return int(exp_string.strip())

    new_string = ""

    if '(' in exp_string:
        mid_string = exp_string[exp_string.find('(')+1:exp_string.rfind(')')]
        new_string = exp_string[:exp_string.find('(')] + str(part1_evaluate_expression(mid_string)) + exp_string[exp_string.rfind(')')+1:]
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

def perform_operation(val1, val2, operator):
    print(val1, val2, operator)
    if operator == "*":
        return str(int(val1) * int(val2))
    if operator == "/":
        return str(int(val1) / int(val2))
    if operator == "+":
        return str(int(val1) + int(val2))
    if operator == "-":
        return str(int(val1) - int(val2))

if __name__=="__main__":
    print(part1_evaluate_expression("1 + 2 * 3 + 4 * 5 + 6"))
    print(part1_evaluate_expression("1 + (2 * 3) + (4 * (5 + 6))"))
    # func1_str = "1 + 2 + (3 + 4)"
    # print("{} == {} - 10".format(func1_str, regular_evaluate_expression(func1_str)))

    # func2_str = "1 + 2 * (3 * (4 + 5))"
    # print("{} == {} - 55".format(func2_str, regular_evaluate_expression(func2_str)))

    # func3_str = "2 * 3"
    # print("{} == {} - 6".format(func3_str, regular_evaluate_expression(func3_str)))

    # func4_str = "2 * 3 + (1 + 2)"
    # print("{} == {} - 9".format(func4_str, regular_evaluate_expression(func4_str)))

    # func5_str = "2 + 3 * 2"
    # print("{} == {} - 8".format(func5_str, regular_evaluate_expression(func5_str)))
