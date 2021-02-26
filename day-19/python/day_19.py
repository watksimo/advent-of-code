def create_rule_dict(line_array):
    rule_dict = {}
    for line in line_array:
        split_line = line.split(": ")
        if '"' in split_line[1]:
            rule_dict[split_line[0]] = split_line[1].replace('"', "")
        else:
            dep_rule = split_line[1].split(" | ")
            dep_rule_array = [[int(rule_no) for rule_no in rule.split(" ")] for rule in dep_rule]
            rule_dict[split_line[0]] = dep_rule_array

    return rule_dict

if __name__=="__main__":
    input_filename = "../test_input.txt"
    f = open(input_filename, 'r')
    line_array = [line.strip() for line in f.readlines()]

    rule_dict = create_rule_dict(line_array)

    print(rule_dict)
