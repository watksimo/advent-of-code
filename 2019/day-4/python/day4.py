def load_input(input_filename):
  f = open(input_filename, "r")
  return [int(_) for _ in f.readline().strip().split("-")]

def solve_part1(min_val, max_val):
  valid_passwords = []
  valid_passwords_2 = []

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
    adj_digits_2 = False
    adj_digits_cnt = 1 # A number by itelf is 1 adj digit (no 0)
    for idx, ch in enumerate(char_array):
      if idx > 0:
        if int(ch) < int(prev_char): char_array[idx] = prev_char
        ch = char_array[idx]
        if int(ch) == int(prev_char):
          adj_digits = True
          adj_digits_cnt += 1
        else:
          if adj_digits_cnt == 2: adj_digits_2 = True
          adj_digits_cnt = 1
      prev_char = ch
    if adj_digits_cnt == 2: adj_digits_2 = True
    new_pass_int = int(''.join(char_array))
    curr_pass_int = new_pass_int

    ## Check password is in range and has adjacent digits
    if min_val <= curr_pass_int <= max_val:
      if adj_digits: valid_passwords.append(curr_pass_int)
      if adj_digits_2: valid_passwords_2.append(curr_pass_int)
    curr_pass_int += 1

  return valid_passwords, valid_passwords_2

if __name__ == '__main__':
  min_val, max_val = load_input("../input.txt")

  valid_passwords, valid_passwords_2 = solve_part1(min_val, max_val)

  # part 1 solution
  print("Part 1 solution: {}".format(len(valid_passwords)))

  # part 2 solution
  print("Part 2 solution: {}".format(len(valid_passwords_2)))

