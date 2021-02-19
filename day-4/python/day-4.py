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
   
def has_required_fields(passport_dict):
    req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    opt_fields = ["cid"]
    return set(req_fields).issubset(set(passport_dict.keys()))

def validate_passport(passport_dict):
    if not 1920 <= int(passport_dict["byr"]) <= 2002: return False
    if not 2010 <= int(passport_dict["iyr"]) <= 2020: return False
    if not 2020 <= int(passport_dict["eyr"]) <= 2030: return False

    if len(passport_dict["hcl"]) != 7 or passport_dict["hcl"][0] != '#': return False
    for cha in passport_dict["hcl"][1:]:
        if not ('0' <= cha <= '9' or 'a' <= cha <= 'f'): return False

    if passport_dict['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']: return False

    try:
        int(passport_dict['pid'])
        hgt_value = int(passport_dict["hgt"][:-2])
        if len(passport_dict['pid']) != 9: return False
    except ValueError:
        return False

    hgt_unit = passport_dict["hgt"][-2:]
    if not (hgt_unit == "cm" and (150 <= hgt_value <= 193)):
        if not (hgt_unit == "in" and (59 <= hgt_value <= 76)):
            return False

    return True

def get_passports_with_fields(input_filename):
    f = open(input_filename, "r")
    input_array = [line.strip() for line in f.readlines()]
    passport_array = normalize_array(input_array)
    return [passport for passport in passport_array if has_required_fields(passport)]

if __name__ == '__main__':
    input_file = "../real-input.txt"
    has_fields_array = get_passports_with_fields(input_file)
    valid_passports = [passport for passport in has_fields_array if validate_passport(passport)]

    print("Part 1: {} passports have the required fields.".format(len(has_fields_array)))
    print("Part 2: {} are valid passports.".format(len(valid_passports)))
