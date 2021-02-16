def normalize_array(input_array):
    pass_array = []
    pass_dict = {}
    for line in input_array:
        if line.strip() == "":
            if pass_dict: pass_array.append(pass_dict)
            pass_dict = {}
        else:
            for elem in line.split(" "):
                key, val = elem.split(":")
                pass_dict[key] = val
   
    if pass_dict: pass_array.append(pass_dict)
    return pass_array
   
def validate_passport(passport_dict):
    req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    opt_fields = ["cid"]
   
    return set(req_fields).issubset(set(passport_dict.keys()))

def part_one(input_filename):
    f = open(input_filename, "r")
    input_array = [line.strip() for line in f.readlines()]
    counter = 0
    passport_array = normalize_array(input_array)
    for pass_dict in passport_array:
        if validate_passport(pass_dict): counter += 1

    return counter
 
if __name__ == '__main__':
    input_file = "../real-input.txt"
    print(part_one(input_file))
    