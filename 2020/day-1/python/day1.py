def solve_part1(input_filename):
  f = open(input_filename, "r")
  line_array = [int(line.strip()) for line in f.readlines()]

  for idx, val in enumerate(line_array):
    for idx2, val2 in enumerate(line_array[idx:]):
      if val + val2 == 2020: return val, val2, val*val2

def solve_part2(input_filename):
  f = open(input_filename, "r")
  line_array = [int(line.strip()) for line in f.readlines()]

  for idx1, val1 in enumerate(line_array):
    for idx2, val2 in enumerate(line_array[idx1:]):
        for idx3, val3 in enumerate(line_array[idx2:]):
          if val1 + val2 + val3 == 2020: return val1, val2, val3, val1*val2*val3

if __name__ == '__main__':
  # part 1 solution
  v1, v2, mult = solve_part1('expense_report.txt')
  print("Part 1: {} + {} = 2020. {} * {} = {}".format(v1, v2, v1, v2, mult))

  # part 2 solution
  v1, v2, v3, mult = solve_part2('expense_report.txt')
  print("Part 2: {} + {} + {} = 2020. {} * {} * {} = {}".format(v1, v2, v3, v1, v2, v3, mult))
  
