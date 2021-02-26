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

def check_password(password, rule):
    return False    # TODO

if __name__=="__main__":
    input_filename = "../test_input.txt"
    f = open(input_filename, 'r')

    rule_array = []
    password_array = []
    file_rules = True

    for line in f.readlines():
        line = line.strip()
        if line == "":
            file_rules = False
        elif file_rules:
            rule_array.append(line)
        else:
            password_array.append(line)

    rule_dict = create_rule_dict(rule_array)

    print(rule_dict)
    print(password_array)
