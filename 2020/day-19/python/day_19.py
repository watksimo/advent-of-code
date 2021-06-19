from iteration_utilities import deepflatten

rule_dict = {}

def create_rule_dict(line_array):
    rule_dict = {}
    for line in line_array:
        split_line = line.split(": ")
        rule_no = int(split_line[0])
        if '"' in split_line[1]:
            rule_dict[rule_no] = split_line[1].replace('"', "")
        else:
            dep_rule = split_line[1].split(" | ")
            dep_rule_array = [[int(rule_no) for rule_no in rule.split(" ")] for rule in dep_rule]
            rule_dict[rule_no] = dep_rule_array

    return rule_dict

def recursive_rule_replace(rule):
    # print(rule)
    if type(rule) == str:
        return rule

    new_rule = rule
    for idx, elem in enumerate(rule):
        if not type(elem) == str:
            for idx2, elem2 in enumerate(elem):
                if type(elem2) == int:
                    # print(f"Elem2: {elem2}")
                    new_rule[idx][idx2] = rule_dict[elem2]
                    return recursive_rule_replace(new_rule)
                if type(elem2) == list:
                    flattened_list = list(deepflatten(elem2))
                    all_chars = True
                    for flat_elem in flattened_list:
                        if type(flat_elem) != str:
                            all_chars = False
                            break
                    if all_chars: continue
                    new_rule[idx][idx2] = recursive_rule_replace(elem2)
                    return recursive_rule_replace(new_rule)

    return rule

def combine_rule_ands(rule_array):
    
    new_array = rule_array
    type_array = [type(_) for _ in rule_array]
    if list not in type_array:
        return "".join(rule_array)

    for idx, test_array in enumerate(rule_array):
        new_array[idx] = combine_rule_ands(test_array)

    return new_array


def check_password(password, rule_key):
    checked_index = 0

    # curr_rule_key = rule_key
    # if rule_dict[curr_rule_key]

    return False    # TODO

if __name__=="__main__":
    input_filename = "../test_input.txt"
    f = open(input_filename, 'r')

    rule_array = []
    password_array = []
    file_rules = True

    # print(password_from_rule([['a','b'], ['c','d']]))

    for line in f.readlines():
        line = line.strip()
        if line == "":
            file_rules = False
        elif file_rules:
            rule_array.append(line)
        else:
            password_array.append(line)

    rule_dict = create_rule_dict(rule_array)

    recursive_rule = recursive_rule_replace(rule_dict[7])
    print(combine_rule_ands(recursive_rule))

    recursive_rule = recursive_rule_replace(rule_dict[6])
    print(combine_rule_ands(recursive_rule))

    recursive_rule = recursive_rule_replace(rule_dict[0])
    print(combine_rule_ands(recursive_rule))

