def part_one(input_filename):
  f = open(input_filename, "r")
  line_array = [line.strip() for line in f.readlines()]

  valid_passwords = 0

  for line in line_array:
    split_one, password = [_.strip() for _ in line.split(":")]
    split_two, rule_letter = split_one.split(" ")
    rule_min, rule_max = [int(_) for _ in split_two.split("-")]

    if rule_min <= password.count(rule_letter) <= rule_max: valid_passwords += 1
  
  return valid_passwords

def part_two(input_filename):
  f = open(input_filename, "r")
  line_array = [line.strip() for line in f.readlines()]

  valid_passwords = 0

  for line in line_array:
    split_one, password = [_.strip() for _ in line.split(":")]
    split_two, rule_letter = split_one.split(" ")
    pos_one, pos_two = [int(_) - 1 for _ in split_two.split("-")]

    if (password[pos_one] == rule_letter) ^ (password[pos_two] == rule_letter) : valid_passwords += 1
  
  return valid_passwords

if __name__ == "__main__":
  p1_passwords = part_one("password_list.txt")
  p2_passwords = part_two("password_list.txt")
  print("Part 1: {} valid passwords.".format(p1_passwords))
  print("Part 2: {} valid passwords.".format(p2_passwords))