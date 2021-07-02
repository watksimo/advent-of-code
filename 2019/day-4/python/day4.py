def load_input(input_filename):
  f = open(input_filename, "r")
  return [int(_) for _ in f.readline().strip().split("-")]

def merge_dicts(dict1, dict2):
  intersects = []
  dict3 = {**dict1, **dict2}
  for key, value in dict3.items():
    if key in dict1 and key in dict2:
      dict3[key] = [value , dict1[key]]
      intersects.append(key)
  return dict3, intersects

def solve_part1(min_val, max_val):
  valid_passwords = []

  # Ensure min < max
  if min_val >= max_val: return valid_passwords

  # Only look at 6 digit numbers
  if min_val < 100000: min_val = 100000
  if max_val > 999999: max_val = 999999

  curr_pass_int = min_val
  while curr_pass_int <= max_val:
    char_array = list(str(curr_pass_int))
    prev_char = None

    # Next valid non-decreasing
    adj_digits = False
    for idx, ch in enumerate(char_array):
      if idx > 0:
        if int(ch) < int(prev_char): char_array[idx] = prev_char
        ch = char_array[idx]
        if int(ch) == int(prev_char): adj_digits = True
      prev_char = ch
    new_pass_int = int(''.join(char_array))
    curr_pass_int = new_pass_int

    ## Check password is in range and has adjacent digits
    if min_val <= curr_pass_int <= max_val and adj_digits:
      valid_passwords.append(curr_pass_int)
    curr_pass_int += 1

  return valid_passwords

if __name__ == '__main__':
  min_val, max_val = load_input("../input.txt")

  # part 1 solution
  valid_passwords = solve_part1(min_val, max_val)
  print("Part 1 solution: {}".format(len(valid_passwords)))

  # part 2 solution
  # print("Part 2 solution: {}".format(solution))

